import time
from utils import *
from constant import *
from pprint import pprint
from client import RE315Client


client = RE315Client(base_url="http://192.168.0.3/", password="passwordhere")
assert client.authenticate(), "Auth Fail"


# Turn on and off LED :))
# status = True
# while True:
#     client.enableLED(status)
#     status = not status


client.startNetworkScan()

while (not client.isScanFininshed()):
    time.sleep(0.5)
    print("Scanning...")
    
print("Scan Finish!")

pprint(client.getScanResult())



# extender2g, extender5g = client.queryData(
#     dataBlocks = [
#         DataBlock(dataID=DataID.MBSSID_MAIN, layer="1,1,0"), # see constant.py
#         DataBlock(dataID=DataID.MBSSID_MAIN, layer="2,1,0")
#     ]
# )
# pprint(toDict(extender2g))
# pprint(toDict(extender5g))



pprint(client.getClients())
pprint(client.getExtenderInfo(2)) # get 2Ghz extender info
pprint(client.getRootAPRSSI(5)) # get 5GHz signal





# print(client.communicate(code=TDDP_READ, data=f"{DataID.DEVICE}|1,0,0"))

# =

# pprint(
#     toDict(client.queryData(dataBlocks=[DataBlock(dataID=DataID.DEVICE)])[0])
# )

