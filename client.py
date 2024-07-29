import re
import time
import httpx
from httpx import codes as HTTPStatusCode

from utils import *
from constant import *
from typing import Optional

import base64
import hashlib
import binascii
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Util.Padding import pad, unpad


CRLF = "\r\n"


class RE315_SU: # $.su
    @staticmethod
    def Encrypt(
        inp: str,
        strDe: str = "RDpbLfCPsJZ7fiv",
        dictionary: str = (
            "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv"
            "3H7NyU84p21BriUWBU43odz3iP4rBL3cD02K"
            "ZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xq"
            "xv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc"
            "8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuR"
            "MO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHo"
            "ic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW"
        )
    ) -> str:
        """$.su.encrypt()"""
        lenInputA = len(inp)
        lenStrDe = len(strDe)
        lenDictionary = len(dictionary)
        length = max(lenInputA, lenStrDe)

        output = []
        
        for idx in range(length):
            a = ord(inp[idx]) if idx < lenInputA else 0xBB
            b = ord(strDe[idx]) if idx < lenStrDe else 0xBB
            output.append(dictionary[(a ^ b) % lenDictionary])

        return "".join(output)

    
    @staticmethod
    def getEncryptedPassword(password: str) -> str: # Web encrypted pwd
        """
        $.su.modelManager.get("localLoginControl").password.doEncrypt()
        """ 
        return __class__.Encrypt(password)
    
    
    @staticmethod
    def passwordEncryption(password: str, inp: str, dictionary: str) -> tuple:
        """
        inp: $.authInfo[3]
        dictionary: $.authInfo[4]
        """
        lgkey = __class__.getEncryptedPassword(password)
        token = __class__.Encrypt( # $.su.encrypt($.authInfo[3], "encryptedpwd", $.authInfo[4]) 
            inp = inp,
            strDe = lgkey,
            dictionary = dictionary
        )
        return (token, lgkey) # LocalStorage
        

    @staticmethod
    def getPasswordHash(password: str, username: str = "admin") -> str:
        return hashlib.md5(
            string = username.encode()+password.encode(),
            usedforsecurity = True
        ).hexdigest()
        



class RE315Encryption:
    def __init__(self, password: str) -> None:
        self.password = password
        self.updateAESKey()
        
        
    def setBasicAuthInfo(self, inp: str, dictionary: str) -> tuple:
        self.passwordHash = RE315_SU.getPasswordHash(self.password)
        token, lgkey = RE315_SU.passwordEncryption(self.password, inp, dictionary)
        return token, lgkey
    

    def setRSAKey(self, RSA_EE: str, RSA_NN: str, seq: int):
        self.RSA_EE, self.RSA_NN, self.seq = RSA_EE.encode(), RSA_NN.encode(), seq
        
    
    def updateAESKey(
        self,
        AES_Key: Optional[bytes] = None,
        AES_InitVector: Optional[bytes] = None
    ):
        self.AES_Key = AES_Key if AES_Key else binascii.b2a_hex(Random.get_random_bytes(8))
        self.AES_InitVector = AES_InitVector if AES_InitVector else binascii.b2a_hex(Random.get_random_bytes(8))
        self.AESKeyString = f"k={self.AES_Key.decode()}&i={self.AES_InitVector.decode()}"
          

    def AES_Encrypt(self, data: str) -> str:
        padded = pad(data.encode(), AES.block_size, style="pkcs7")
        cipher = AES.new(self.AES_Key, AES.MODE_CBC, self.AES_InitVector)
        return base64.b64encode(cipher.encrypt(padded)).decode()


    def AES_Decrypt(self, data: str) -> str:
        cipher = AES.new(self.AES_Key, AES.MODE_CBC, self.AES_InitVector)
        decrypted = cipher.decrypt(base64.b64decode(data))
        return unpad(decrypted, AES.block_size, style="pkcs7").decode()
    
    
    def RSA_Encrypt(self, data: str) -> str:
        n = int(self.RSA_NN, 16)
        e = int(self.RSA_EE, 16)

        key = RSA.construct((n, e))
        cipher = PKCS1_v1_5.new(key)
        
        result = cipher.encrypt(data.encode()).hex()
        return result
       
    
    def getEncodedAESKey(self) -> str:
        """$.su.encryptor.getEncodeAESKey()"""
        return self.RSA_Encrypt(self.AESKeyString)
    
    
    def getSignature(self, dataSize: int) -> str:
        """$.su.encryptor.getSignature()"""
        string = f"{self.AESKeyString}&s={self.seq+dataSize}"     
        chunkSize = 53
        signatureChunks = [
            self.RSA_Encrypt(string[pos:pos + chunkSize])
            for pos in range(0, len(string), chunkSize)
        ]
        return "".join(signatureChunks)
        
    
    def encryptData(self, data: str) -> str:
        """$.su.encryptor.dataEncrypt(data)"""
        encryptedData = self.AES_Encrypt(data)
        signature = self.getSignature(len(encryptedData))
        return f"sign={signature}{CRLF}data={encryptedData}"


    def decryptData(self, data: str) -> str:
        """$.su.encryptor.dataDecrypt(data)"""
        return self.AES_Decrypt(data)




class RE315Auth:
    def __init__(self, base_url: str, password: str, timeout: Optional[int] = None) -> None:
        self.httpClient = httpx.Client(
            base_url = base_url,
            headers = {
                "Referer": base_url,
                "Content-Type": "text/html;charset=UTF-8"
            },
            timeout = timeout
        )
        self.token = None
        self.crypt = RE315Encryption(password)
        self.useEncryption = False

    
    def communicate(
            self,
            code: int,
            data: Optional[str] = None,
            isAsync: bool = False,
            ignoreError: bool = False
        ) -> listStr:
        getResponse = lambda: self.httpClient.post(
            url = "/",
            content = (self.crypt.encryptData(data) if self.useEncryption else data.encode()) if data else data,
            params = {
                "code": code,
                "asyn": 1 if isAsync else 0,
                "id": self.token
            }
        )
        response = getResponse()

        for _ in range(5): # Encryption reset after some period of time.
            result = response.content.decode().strip()
            if self.useEncryption:
                if response.is_success:
                    result = self.crypt.decryptData(result).strip()
                    break
                elif response.status_code in [HTTPStatusCode.UNAUTHORIZED, HTTPStatusCode.FORBIDDEN]:
                    print(f"Reset Encryption!")
                    time.sleep(3)
                    self.useEncryption = False
                    if self.authenticate():
                        response = getResponse()
                        print(f"Success!")
                        continue
                    else:
                        raise Exception("Auth failed :((")
                else:
                    if ignoreError:
                        break
                    else:
                        raise Exception(f"status {response.status_code}!\n Content: {response.content} ")
            else:
                break
        return result.split(CRLF)
        
    
    def enableGDPR(self):
        return self.communicate(code=HTTP_OP_GDPRCFG, data="enable")


    def syncGDPR(self):
        return self.communicate(code=HTTP_OP_GDPRCFG, data=f"set {self.crypt.getEncodedAESKey()}")   
           
    
    def getAuthInfo(self) -> tuple:
        """
        - status: 6 if another session is active else 4.
        - tries: number of failed authentication attempts (max 10).
        - inp, dictionary: $.authInfo[3], $.authInfo[4].
        """
        _, status, tries, inp, dictionary, _  = self.communicate(code=TDDP_AUTH, isAsync=True)
        return int(status), int(tries), inp, dictionary
    
    
    def getRSAKey(self) -> tuple:
        _, RSA_EE, RSA_NN, seq = self.communicate(code=HTTP_OP_GDPRCFG, data="get")
        return RSA_EE, RSA_NN, int(seq)
    
         
    def authenticate(self):   
        self.enableGDPR()
        self.token = None
        self.crypt.updateAESKey()
        self.crypt.setRSAKey(*self.getRSAKey())
        
        _, tries, inp, dictionary = self.getAuthInfo()
        if tries == 10: raise Exception("You have exceeded 10 login attempts. Please try again in 2 hours.")

        self.token, self.lgkey = self.crypt.setBasicAuthInfo(inp, dictionary)
        result = self.communicate(code=TDDP_AUTH)

        if len(result) > 1 and result[1] == "00003":
            print(f"Wrong Password! ({int(result[2])}/10 attempts)")
            result = False
        else:
            result = self.syncGDPR() == ["00000"]
            self.useEncryption = True
        
        return result



class RE315Request(RE315Auth):
    def queryData(self, dataBlocks: list[DataBlock]) -> list[listStr]:
        response = self.communicate(code=TDDP_READ, data="#".join([f"{block.dataID}|{block.layer}" for block in dataBlocks]))[1:]
        idxs = [idx for idx, line in enumerate(response) if re.match(r"id\s+\d+\|\d+,\d+,\d+", line)] + [len(response)]
        sliced = [response[start+1:stop] for (start, stop) in zip(idxs, idxs[1:])]
        return sliced


    def writeData(self, dataBlocks: list[DataBlock]) -> bool:
        response = self.communicate(
            code = TDDP_WRITE,
            data = "\n".join(
                [
                    f"id {dataBlock.dataID}|{dataBlock.layer}\n{dataBlock.content}"
                    for dataBlock in dataBlocks
                ]
            )
        )
        return True if response == ["00000"] else False
    
    
    def executeInstruction(self, command: str):
        return self.communicate(code=TDDP_INSTRUCT, data=command)[1:]
    
    
    
class RE315Client(RE315Request):
    def startNetworkScan(self):
        self.executeInstruction("wlan scan 2g")
        self.executeInstruction("wlan scan 5g")
        
    
    def isScanFininshed(self):
        return int(self.executeInstruction("wlan scanStatus 2g")[0]) + \
               int(self.executeInstruction("wlan scanStatus 5g")[0]) == 2
               
    
    def getScanResult(self):
        response = self.queryData(
            dataBlocks = [
                DataBlock(dataID=DataID.WLAN_AP_LIST, layer="1,0,0"), # 2Ghz
                DataBlock(dataID=DataID.WLAN_AP_LIST, layer="2,0,0")  # 5Ghz
            ]
        )
        firstEOL = ("cBssid", "00-00-00-00-00-00")
        return [parseList(band, firstEOL) for band in response]
        
    
    def getDHCPInfo(self) -> dict:
        return toDict(self.queryData([DataBlock(DataID.DHCPC)])[0])    

    
    def getExtenderMAC(self, band: int) -> str:
        return self.executeInstruction(f"wlan getWirelessMac {band}g")[0]    


    def getRootAPRSSI(self, band: int) -> RE315SignalLevel:
        return rssiConv(int(self.executeInstruction(f"wlan getRootApRssi {band}g")[0]))
          
    
    def getBasicWLANInfo(self, band: int) -> dict:
        response = self.queryData(
            [DataBlock(DataID.WLAN_BASIC, "1,0,0" if band == 2 else "2,0,0")]
        )[0]
        return toDict(response)
    
    
    def getExtenderChannel(self, band: int) -> int:
        return int(self.executeInstruction(f"wlan channel {band}g")[0])
    
    
    def getExtenderInfo(self, band: int) -> dict:
        response = self.queryData(
            [DataBlock(DataID.MBSSID_MAIN, "1,1,0" if band == 2 else "2,1,0")]
        )[0]
        return toDict(response)
    
    
    def getClients(self) -> list[dict]:
        result = []
        for line in self.queryData([DataBlock(DataID.STARTTABLE)])[0]:
            dataType, data = line.split(maxsplit=1)
            data = data.split()
            if len(data) < 2: continue
            idx, content = int(data[0]), data[1]
                    
            if dataType == "ip" and content != "0.0.0.0":
                result.append({"ip": content})
                continue
                
            if idx < len(result):
                result[idx][dataType] = int(content) if content.isnumeric() else content

        return result
                        
                
    def enableLED(self, enable: bool = True) -> bool:
        response = self.writeData(
            [DataBlock(dataID=DataID.LED, content=f"enable {1 if enable else 0}")]
        )
        return response