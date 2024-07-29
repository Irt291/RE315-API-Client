"""frame.js's constant"""

from enum import IntEnum
from dataclasses import dataclass


listStr = list[str]
listDict = list[dict]


# endpoint
TDDP_INSTRUCT = 0
TDDP_WRITE = 1
TDDP_READ = 2

TDDP_REBOOT = 6
TDDP_AUTH = 7
TDDP_GETPEERMAC = 8
TDDP_LOGOUT = 11
HTTP_OP_GDPRCFG = 16 



class WIFICoverage:
    Maximum = 1
    Intermediate = 2
    Minimum = 3
    
    
class DeviceConnectionType:
    _2GHZ = 1
    WIRED = 2
    _5GHZ = 3


# req: TDDP_READ {dataid}|{layers}
# batchreq: {dataid1}|{layers1}#{dataid2}|{layers2}#{dataid3}|{layers3}
# exp: /?code=2 (TDDP_READ)
# requestContent:
#   32|1,0,0  (32 = WLAN_BASIC_DATA_ID)


# req: TDDP_WRITE id {dataid}|{layers}\n{content}
# batchreq:
#   id {dataid1}|{layers1}
#   some content 
#   id {dataid2}|{layers2}
#   some content 


# exp /?code=1 (TDDP_WRITE)
# requestContent:
#   id 112|1,0,0  (112 = LED)
#   enable 1 


class DataID(IntEnum):
    DEVICE = 0
    SYSTEM = 1
    SYSTEM_LOG = 2
    EXCEPT_LOG = 3
    LAN = 4
    LCLPORT = 5
    LCLHOST = 6
    RMTHOST = 7
    DHCPS = 8
    DHCPS_LEASE = 9
    TPDOMAIN = 10
    FACTORY = 11
    STACTRLTBL = 12
    STARTTABLE = 13
    STATIC_ROUTE = 14
    DYNAMIC_ROUTE = 15
    SYSTEM_ROUTE = 16
    NAPT_ALG = 17
    NAPT_DMZ = 18
    NAPT_IGD = 19
    NAPT_IGD_MAPPING = 20
    NAPT_VSERVER = 21
    LINK = 22
    LINK_STATUS = 23
    STATIC_IP = 24
    DHCPC = 25
    PPPOE = 26
    PPPOE_LASTDIAL = 27
    SNTPC_CONFIG = 28
    SNTPC_TIME = 29
    PARENT_CTL = 30
    BEHAVMANG_CONFIG = 31
    WLAN_BASIC = 32
    MBSSID_MAIN = 33
    WLAN_AP_LIST = 34
    IPTV = 35
    PPTP = 36
    L2TP = 37
    DDNS = 38
    DDNS_STATUS = 39
    IPV6_MODE = 40
    IPV6_WAN_INTERFACE = 41
    IPV6_WAN_ADDR = 42
    IPV6_WAN_DNS = 43
    IPV6_PPPOE = 44
    IPV6_WAN_STATUS = 45
    IPV6_PREFIX_DELEGATION = 46
    IPV6_LAN_PREFIX = 47
    IPV6_LAN_STATUS = 48
    MANUFACTURE_MODE = 49
    LANGUAGE = 50
    HW_NAT = 57
    RE_QS = 58
    WIFI = 110
    DST = 111
    LED = 112
    NIGHT_MODE = 113
    SCHEDULE_REBOOT = 114
    POWER_SCHEDULE = 115
    HIGH_SPEED = 122
    BLACK_LIST = 59
    WHITE_LIST = 60
    CLOUD_BASIC = 65
    CLOUD_FW_UPGRADE = 66
    CLOUD_OWNER = 67
    CLOUD_CURRENT_USER_CFG = 68
    CLOUD_DDNS = 69
    CLOUD_CURRENT_USER = 70
    CLOUD_SVR_CONFIG = 71
    WEB_SWITCH = 85
    REGION = 89
    
    

@dataclass
class DataBlock:
    dataID: DataID
    layer: str = "1,0,0"
    content: str = ""
    
    
    
        
# $.su.modelManager._map    

    
# function DataBlock() {
#     this.DEVICE_1_0_0 = {
#         id: DEVICE_DATA_ID,
#         layers: [1, 0, 0],
#         fullName: "",
#         facturer: "",
#         modelName: "",
#         modelVer: "",
#         softVer: "",
#         hardVer: "",
#         prodId: "",
#         languId: "",
#         countryId: "",
#         mainVer: "",
#         minorVer: "",
#         oemId: ""
#     }, this.SYSTEM_1_0_0 = {
#         id: SYSTEM_DATA_ID,
#         layers: [1, 0, 0],
#         authKey: "",
#         setWzd: "",
#         mode: "",
#         logLevel: "",
#         fastpath: "",
#         mac: []
#     }, this.SYSTEM_LOG_1_0_0 = {
#         id: SYSTEM_LOG_DATA_ID,
#         layers: [1, 0, 0],
#         num: "",
#         showType: "",
#         list: [{
#             level: "",
#             days: "",
#             hours: "",
#             mins: "",
#             secs: "",
#             msecs: "",
#             msg: "",
#             type: ""
#         }]
#     }, this.EXCEPT_LOG_1_0_0 = {
#         id: EXCEPT_LOG_DATA_ID,
#         layers: [1, 0, 0],
#         num: "",
#         list: [{
#             msg: ""
#         }]
#     }, this.LAN_1_0_0 = {
#         id: LAN_DATA_ID,
#         layers: [1, 0, 0],
#         ip: "",
#         mask: "",
#         mode: "",
#         dns: [],
#         gateway: ""
#     }, this.LCLPORT_1_0_0 = {
#         id: LCLPORT_DATA_ID,
#         layers: [1, 0, 0],
#         port: ""
#     }, this.LCLHOST_1_0_0 = {
#         id: LCLHOST_DATA_ID,
#         layers: [1, 0, 0],
#         enableAll: "",
#         mac: []
#     }, this.RMTHOST_1_0_0 = {
#         id: RMTHOST_DATA_ID,
#         layers: [1, 0, 0],
#         port: "",
#         rule: "",
#         addr: ""
#     }, this.DHCPS_1_0_0 = {
#         id: DHCPS_DATA_ID,
#         layers: [1, 0, 0],
#         mode: "",
#         poolStart: "",
#         poolEnd: "",
#         leaseTime: "",
#         dns: [],
#         gateway: "",
#         hostName: ""
#     }, this.DHCPS_LEASE_1_0_0 = {
#         id: DHCPS_LEASE_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             hostName: "",
#             mac: "",
#             reserved: "",
#             state: "",
#             ip: "",
#             expires: ""
#         }]
#     }, this.TPDOMAIN_1_0_0 = {
#         id: TPDOMAIN_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         name: ""
#     }, this.FACTORY_1_0_0 = {
#         id: FACTORY_DATA_ID,
#         layers: [1, 0, 0],
#         lanIp: "",
#         lanMask: "",
#         authKey: ""
#     }, this.STACTRLTBL_1_0_0 = {
#         id: STACTRLTBL_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             ip: "",
#             mac: "",
#             reserved: "",
#             bindEntry: "",
#             staMgtEntry: "",
#             name: "",
#             blocked: ""
#         }]
#     }, this.STARTTABLE_1_0_0 = {
#         id: STARTTABLE_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             ip: "",
#             mac: "",
#             reserved: "",
#             bindEntry: "",
#             staMgtEntry: "",
#             type: "",
#             online: "",
#             name: "",
#             DevType: ""
#         }]
#     }, this.STATIC_ROUTE_1_0_0 = {
#         id: STATIC_ROUTE_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             enable: "",
#             net: "",
#             mask: "",
#             gateway: ""
#         }]
#     }, this.DYNAMIC_ROUTE_1_0_0 = {
#         id: DYNAMIC_ROUTE_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             net: "",
#             mask: "",
#             gateway: ""
#         }]
#     }, this.SYSTEM_ROUTE_1_0_0 = {
#         id: SYSTEM_ROUTE_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             net: "",
#             gateway: "",
#             mask: "",
#             netif: ""
#         }]
#     }, this.NAPT_ALG_1_0_0 = {
#         id: NAPT_ALG_DATA_ID,
#         layers: [1, 0, 0],
#         ftpAlgEnable: "",
#         pptpAlgEnable: "",
#         rtspAlgEnable: "",
#         sipAlgEnable: "",
#         ipsecAlgEnable: "",
#         h323AlgEnable: ""
#     }, this.NAPT_DMZ_1_0_0 = {
#         id: NAPT_DMZ_DATA_ID,
#         layers: [1, 0, 0],
#         dmzEnable: "",
#         dmzClient: ""
#     }, this.NAPT_IGD_1_0_0 = {
#         id: NAPT_IGD_DATA_ID,
#         layers: [1, 0, 0],
#         igdEnable: ""
#     }, this.NAPT_IGD_MAPPING_1_0_0 = {
#         id: NAPT_IGD_MAPPING_DATA_ID,
#         layers: [1, 0, 0],
#         num: "",
#         list: [{
#             extPort: "",
#             intPort: "",
#             ptc: "",
#             enabled: "",
#             leaseDuration: "",
#             leaseTimer: "",
#             rmtHost: "",
#             client: "",
#             desc: ""
#         }]
#     }, this.NAPT_VSERVER_1_0_0 = {
#         id: NAPT_VSERVER_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             vsEntryEnable: "",
#             vsLclIp: "",
#             vsRmtIp: "",
#             vsLclPort: "",
#             vsRmtPort: "",
#             vsOpenPortS: "",
#             vsOpenPortE: "",
#             vsPtc: ""
#         }]
#     }, this.LINK_1_0_0 = {
#         id: LINK_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         wirelessWan: "",
#         linkMode: "",
#         linkType: ""
#     }, this.LINK_STATUS_1_0_0 = {
#         id: LINK_STATUS_DATA_ID,
#         layers: [1, 0, 0],
#         ip: "",
#         mask: "",
#         gateway: "",
#         dns: [],
#         status: "",
#         code: "",
#         upTime: "",
#         inPkts: "",
#         inOctets: "",
#         outPkts: "",
#         outOctets: "",
#         inRates: "",
#         outRates: "",
#         dualMode: "",
#         dualIp: "",
#         dualMask: "",
#         dualGateway: "",
#         dualDns: [],
#         dualCode: "",
#         dualStatus: ""
#     }, this.STATIC_IP_1_0_0 = {
#         id: STATIC_IP_DATA_ID,
#         layers: [1, 0, 0],
#         ip: "",
#         mask: "",
#         gateway: "",
#         dns: [],
#         mtu: ""
#     }, this.DHCPC_1_0_0 = {
#         id: DHCPC_DATA_ID,
#         layers: [1, 0, 0],
#         name: "",
#         dns: [],
#         mtu: "",
#         ucast: "",
#         manualDns: "",
#         lastIp: ""
#     }, this.PPPOE_1_0_0 = {
#         id: PPPOE_DATA_ID,
#         layers: [1, 0, 0],
#         svName: "",
#         acName: "",
#         name: "",
#         paswd: "",
#         fixipEnb: "",
#         fixip: "",
#         manualDns: "",
#         dns: [],
#         lcpMru: "",
#         linkType: "",
#         dialMode: "",
#         maxIdleTime: "",
#         sndConnType: "",
#         staticSndIp: "",
#         staticSndMask: ""
#     }, this.PPPOE_LASTDIAL_1_0_0 = {
#         id: PPPOE_LASTDIAL_DATA_ID,
#         layers: [1, 0, 0],
#         acMac: "",
#         reserved: "",
#         sessionid: "",
#         dialMode: "",
#         ncTimes: ""
#     }, this.SNTPC_CONFIG_1_0_0 = {
#         id: SNTPC_CONFIG_DATA_ID,
#         layers: [1, 0, 0],
#         timeZone: "",
#         type: "",
#         ntpSvr1: "",
#         ntpSvr2: "",
#         hour24Enable: ""
#     }, this.SNTPC_TIME_1_0_0 = {
#         id: SNTPC_TIME_DATA_ID,
#         layers: [1, 0, 0],
#         year: "",
#         month: "",
#         day: "",
#         hour: "",
#         minute: "",
#         second: ""
#     }, this.PARENT_CTL_1_0_0 = {
#         id: PARENT_CTL_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         mon: "",
#         tue: "",
#         wed: "",
#         thu: "",
#         fri: "",
#         sat: "",
#         sun: "",
#         list: [{
#             mac: "",
#             reserved: ""
#         }]
#     }, this.BEHAVMANG_CONFIG_1_0_0 = {
#         id: BEHAVMANG_CONFIG_DATA_ID,
#         layers: [1, 0, 0],
#         bhavEnable: "",
#         bhavRule: ""
#     }, this.WLAN_BASIC_1_0_0 = {
#         id: WLAN_BASIC_DATA_ID,
#         layers: [1, 0, 0],
#         uBand: "",
#         bEnabled: "",
#         uApMode: "",
#         uRegionIndex: "",
#         uChannel: "",
#         uBgnMode: "",
#         uChannelWidth: "",
#         adv: {
#             uRTSThreshold: "",
#             uFragThreashold: "",
#             uBeaconInterval: "",
#             uPower: "",
#             uDTIMInterval: "",
#             bWMEEnabled: "",
#             bIsolationEnabled: "",
#             bShortPrmbleDisabled: "",
#             bShortGI: ""
#         },
#         apc: {
#             bBridgeEnabled: "",
#             cBridgedSsid: "",
#             cBridgedBssid: "",
#             uWepIndex: "",
#             uSecurityType: "",
#             cPassWD: "",
#             uDetect: "",
#             uPSKEncryptType: "",
#             bSupportMesh: "",
#             cTPIE: "",
#             uNodeId: "",
#             bSupportEasymesh: "",
#             reserved: ""
#         },
#         guest: {
#             bLanAccess: "",
#             uDuration: "",
#             bSetOpenTime: "",
#             uMaxUploadSpeed: "",
#             uMaxDownloadSpeed: "",
#             uAllowTimeMode: "",
#             uTimeTable: []
#         },
#         bTurboOn: ""
#     }, this.WLAN_BASIC_2_0_0 = {
#         id: WLAN_BASIC_DATA_ID,
#         layers: [2, 0, 0],
#         uBand: "",
#         bEnabled: "",
#         uApMode: "",
#         uRegionIndex: "",
#         uChannel: "",
#         uBgnMode: "",
#         uChannelWidth: "",
#         adv: {
#             uRTSThreshold: "",
#             uFragThreashold: "",
#             uBeaconInterval: "",
#             uPower: "",
#             uDTIMInterval: "",
#             bWMEEnabled: "",
#             bIsolationEnabled: "",
#             bShortPrmbleDisabled: "",
#             bShortGI: ""
#         },
#         apc: {
#             bBridgeEnabled: "",
#             cBridgedSsid: "",
#             cBridgedBssid: "",
#             uWepIndex: "",
#             uSecurityType: "",
#             cPassWD: "",
#             uDetect: "",
#             uPSKEncryptType: "",
#             bSupportMesh: "",
#             cTPIE: "",
#             uNodeId: "",
#             bSupportEasymesh: "",
#             reserved: ""
#         },
#         guest: {
#             bLanAccess: "",
#             uDuration: "",
#             bSetOpenTime: "",
#             uMaxUploadSpeed: "",
#             uMaxDownloadSpeed: "",
#             uAllowTimeMode: "",
#             uTimeTable: []
#         },
#         bTurboOn: ""
#     }, this.MBSSID_MAIN_1_1_0 = {
#         id: MBSSID_MAIN_DATA_ID,
#         layers: [1, 1, 0],
#         uUnit: "",
#         cSsidPrefix: "",
#         uRadiusIp: "",
#         uRadiusGKUpdateIntvl: "",
#         uPskGKUpdateIntvl: "",
#         privacyRcd: [{
#             uKeyLength: "",
#             cKeyVal: ""
#         }],
#         uRadiusPort: "",
#         uKeyType: "",
#         uDefaultKey: "",
#         bEnable: "",
#         bBcastSsid: "",
#         cSsid: "",
#         bSecurityEnable: "",
#         uAuthType: "",
#         uWEPSecOpt: "",
#         uRadiusSecOpt: "",
#         uPSKSecOpt: "",
#         uRadiusEncryptType: "",
#         uPSKEncryptType: "",
#         cRadiusSecret: "",
#         cPskSecret: "",
#         bSecCheck: "",
#         wps: {
#             bEnabled: "",
#             cUsrPIN: "",
#             bConfigured: "",
#             bIsLocked: "",
#             bPinEnabled: ""
#         }
#     }, this.MBSSID_MAIN_1_2_0 = {
#         id: MBSSID_MAIN_DATA_ID,
#         layers: [1, 2, 0],
#         uUnit: "",
#         cSsidPrefix: "",
#         uRadiusIp: "",
#         uRadiusGKUpdateIntvl: "",
#         uPskGKUpdateIntvl: "",
#         privacyRcd: [{
#             uKeyLength: "",
#             cKeyVal: ""
#         }],
#         uRadiusPort: "",
#         uKeyType: "",
#         uDefaultKey: "",
#         bEnable: "",
#         bBcastSsid: "",
#         cSsid: "",
#         bSecurityEnable: "",
#         uAuthType: "",
#         uWEPSecOpt: "",
#         uRadiusSecOpt: "",
#         uPSKSecOpt: "",
#         uRadiusEncryptType: "",
#         uPSKEncryptType: "",
#         cRadiusSecret: "",
#         cPskSecret: "",
#         bSecCheck: "",
#         wps: {
#             bEnabled: "",
#             cUsrPIN: "",
#             bConfigured: "",
#             bIsLocked: ""
#         }
#     }, this.MBSSID_MAIN_1_3_0 = {
#         id: MBSSID_MAIN_DATA_ID,
#         layers: [1, 3, 0],
#         uUnit: "",
#         cSsidPrefix: "",
#         uRadiusIp: "",
#         uRadiusGKUpdateIntvl: "",
#         uPskGKUpdateIntvl: "",
#         privacyRcd: [{
#             uKeyLength: "",
#             cKeyVal: ""
#         }],
#         uRadiusPort: "",
#         uKeyType: "",
#         uDefaultKey: "",
#         bEnable: "",
#         bBcastSsid: "",
#         cSsid: "",
#         bSecurityEnable: "",
#         uAuthType: "",
#         uWEPSecOpt: "",
#         uRadiusSecOpt: "",
#         uPSKSecOpt: "",
#         uRadiusEncryptType: "",
#         uPSKEncryptType: "",
#         cRadiusSecret: "",
#         cPskSecret: "",
#         bSecCheck: "",
#         wps: {
#             bEnabled: "",
#             cUsrPIN: "",
#             bConfigured: "",
#             bIsLocked: ""
#         }
#     }, this.MBSSID_MAIN_2_1_0 = {
#         id: MBSSID_MAIN_DATA_ID,
#         layers: [2, 1, 0],
#         uUnit: "",
#         cSsidPrefix: "",
#         uRadiusIp: "",
#         uRadiusGKUpdateIntvl: "",
#         uPskGKUpdateIntvl: "",
#         privacyRcd: [{
#             uKeyLength: "",
#             cKeyVal: ""
#         }],
#         uRadiusPort: "",
#         uKeyType: "",
#         uDefaultKey: "",
#         bEnable: "",
#         bBcastSsid: "",
#         cSsid: "",
#         bSecurityEnable: "",
#         uAuthType: "",
#         uWEPSecOpt: "",
#         uRadiusSecOpt: "",
#         uPSKSecOpt: "",
#         uRadiusEncryptType: "",
#         uPSKEncryptType: "",
#         cRadiusSecret: "",
#         cPskSecret: "",
#         bSecCheck: "",
#         wps: {
#             bEnabled: "",
#             cUsrPIN: "",
#             bConfigured: "",
#             bIsLocked: "",
#             bPinEnabled: ""
#         }
#     }, this.MBSSID_MAIN_2_2_0 = {
#         id: MBSSID_MAIN_DATA_ID,
#         layers: [2, 2, 0],
#         uUnit: "",
#         cSsidPrefix: "",
#         uRadiusIp: "",
#         uRadiusGKUpdateIntvl: "",
#         uPskGKUpdateIntvl: "",
#         privacyRcd: [{
#             uKeyLength: "",
#             cKeyVal: ""
#         }],
#         uRadiusPort: "",
#         uKeyType: "",
#         uDefaultKey: "",
#         bEnable: "",
#         bBcastSsid: "",
#         cSsid: "",
#         bSecurityEnable: "",
#         uAuthType: "",
#         uWEPSecOpt: "",
#         uRadiusSecOpt: "",
#         uPSKSecOpt: "",
#         uRadiusEncryptType: "",
#         uPSKEncryptType: "",
#         cRadiusSecret: "",
#         cPskSecret: "",
#         bSecCheck: "",
#         wps: {
#             bEnabled: "",
#             cUsrPIN: "",
#             bConfigured: "",
#             bIsLocked: ""
#         }
#     }, this.MBSSID_MAIN_2_3_0 = {
#         id: MBSSID_MAIN_DATA_ID,
#         layers: [2, 3, 0],
#         uUnit: "",
#         cSsidPrefix: "",
#         uRadiusIp: "",
#         uRadiusGKUpdateIntvl: "",
#         uPskGKUpdateIntvl: "",
#         privacyRcd: [{
#             uKeyLength: "",
#             cKeyVal: ""
#         }],
#         uRadiusPort: "",
#         uKeyType: "",
#         uDefaultKey: "",
#         bEnable: "",
#         bBcastSsid: "",
#         cSsid: "",
#         bSecurityEnable: "",
#         uAuthType: "",
#         uWEPSecOpt: "",
#         uRadiusSecOpt: "",
#         uPSKSecOpt: "",
#         uRadiusEncryptType: "",
#         uPSKEncryptType: "",
#         cRadiusSecret: "",
#         cPskSecret: "",
#         bSecCheck: "",
#         wps: {
#             bEnabled: "",
#             cUsrPIN: "",
#             bConfigured: "",
#             bIsLocked: ""
#         }
#     }, this.WLAN_AP_LIST_1_0_0 = {
#         id: WLAN_AP_LIST_DATA_ID,
#         layers: [1, 0, 0],
#         apEntry: [{
#             cBssid: "",
#             cSsid: "",
#             uRssi: "",
#             uChannel: "",
#             uAuthMode: "",
#             uBgnMode: "",
#             uChanWidth: "",
#             uCipherType: "",
#             support_mesh: "",
#             node_id: "",
#             tpie: "",
#             support_easymesh: "",
#             reserved: ""
#         }],
#         uApCnt: ""
#     }, this.WLAN_AP_LIST_2_0_0 = {
#         id: WLAN_AP_LIST_DATA_ID,
#         layers: [2, 0, 0],
#         apEntry: [{
#             cBssid: "",
#             cSsid: "",
#             uRssi: "",
#             uChannel: "",
#             uAuthMode: "",
#             uBgnMode: "",
#             uChanWidth: "",
#             uCipherType: "",
#             support_mesh: "",
#             node_id: "",
#             tpie: "",
#             support_easymesh: "",
#             reserved: ""
#         }],
#         uApCnt: ""
#     }, this.IPTV_1_0_0 = {
#         id: IPTV_DATA_ID,
#         layers: [1, 0, 0],
#         uMode: "",
#         uBridgePorts: "",
#         uService: [{
#             uVid: "",
#             uVlanPriority: "",
#             uMemberPorts: "",
#             bTagEnable: "",
#             uServiceType: ""
#         }]
#     }, this.PPTP_1_0_0 = {
#         id: PPTP_DATA_ID,
#         layers: [1, 0, 0],
#         userName: "",
#         passwd: "",
#         domainIp: "",
#         bDhcp: "",
#         ip: "",
#         mask: "",
#         gateway: "",
#         dns: [],
#         mtu: "",
#         linkType: "",
#         maxIdleTime: ""
#     }, this.L2TP_1_0_0 = {
#         id: L2TP_DATA_ID,
#         layers: [1, 0, 0],
#         userName: "",
#         passwd: "",
#         domainIp: "",
#         bDhcp: "",
#         ip: "",
#         mask: "",
#         gateway: "",
#         dns: [],
#         mtu: "",
#         linkType: "",
#         maxIdleTime: ""
#     }, this.DDNS_1_0_0 = {
#         id: DDNS_DATA_ID,
#         layers: [1, 0, 0],
#         mode: "",
#         serviceList: [{
#             enable: "",
#             username: "",
#             password: "",
#             domainName: "",
#             ip: "",
#             status: ""
#         }]
#     }, this.DDNS_STATUS_1_0_0 = {
#         id: DDNS_STATUS_DATA_ID,
#         layers: [1, 0, 0],
#         status: []
#     }, this.IPV6_MODE_1_0_0 = {
#         id: IPV6_MODE_DATA_ID,
#         layers: [1, 0, 0],
#         mode: ""
#     }, this.IPV6_WAN_INTERFACE_1_0_0 = {
#         id: IPV6_WAN_INTERFACE_DATA_ID,
#         layers: [1, 0, 0],
#         interfaceType: "",
#         ipGetMethod: ""
#     }, this.IPV6_WAN_ADDR_1_0_0 = {
#         id: IPV6_WAN_ADDR_DATA_ID,
#         layers: [1, 0, 0],
#         wanIp: "",
#         wanPrefixLen: "",
#         gateway: ""
#     }, this.IPV6_WAN_DNS_1_0_0 = {
#         id: IPV6_WAN_DNS_DATA_ID,
#         layers: [1, 0, 0],
#         dnsGetMethod: "",
#         dns: []
#     }, this.IPV6_PPPOE_1_0_0 = {
#         id: IPV6_PPPOE_DATA_ID,
#         layers: [1, 0, 0],
#         shareSession: "",
#         username: "",
#         password: ""
#     }, this.IPV6_WAN_STATUS_1_0_0 = {
#         id: IPV6_WAN_STATUS_DATA_ID,
#         layers: [1, 0, 0],
#         status: "",
#         errorCode: "",
#         interfaceType: "",
#         ipGetMethod: "",
#         raReceived: "",
#         getIpWithDhcp: "",
#         getDnsWithDhcp: "",
#         globalIp: "",
#         prefixAddr: "",
#         prefixLen: "",
#         gateway: "",
#         dns: [],
#         linkLocalIp: ""
#     }, this.IPV6_PREFIX_DELEGATION_1_0_0 = {
#         id: IPV6_PREFIX_DELEGATION_DATA_ID,
#         layers: [1, 0, 0],
#         enable: ""
#     }, this.IPV6_LAN_PREFIX_1_0_0 = {
#         id: IPV6_LAN_PREFIX_DATA_ID,
#         layers: [1, 0, 0],
#         prefixAddr: "",
#         prefixLen: ""
#     }, this.IPV6_LAN_STATUS_1_0_0 = {
#         id: IPV6_LAN_STATUS_DATA_ID,
#         layers: [1, 0, 0],
#         linkLocalIp: "",
#         prefixAddr: "",
#         prefixLen: ""
#     }, this.MANUFACTURE_MODE_1_0_0 = {
#         id: MANUFACTURE_MODE_DATA_ID,
#         layers: [1, 0, 0],
#         mode: ""
#     }, this.LANGUAGE_1_0_0 = {
#         id: LANGUAGE_DATA_ID,
#         layers: [1, 0, 0],
#         currentLanguage: "",
#         languageList: "",
#         setByUser: ""
#     }, this.HW_NAT_1_0_0 = {
#         id: HW_NAT_DATA_ID,
#         layers: [1, 0, 0],
#         enable: ""
#     }, this.SCHEDULE_REBOOT = {
#         id: SCHEDULE_REBOOT_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         cycle: "",
#         time: "",
#         day: ""
#     }, this.DST_1_0_0 = {
#         id: DST_DATA_ID,
#         layers: [1, 0, 0],
#         dstEnable: "",
#         startMonth: "",
#         startWeek: "",
#         startDay: "",
#         startHour: "",
#         endMonth: "",
#         endWeek: "",
#         endDay: "",
#         endHour: "",
#         dstStatus: ""
#     }, this.LED_1_0_0 = {
#         id: LED_DATA_ID,
#         layers: [1, 0, 0],
#         enable: ""
#     }, this.WIFI_1_0_0 = {
#         id: WIFI_DATA_ID,
#         layers: [1, 0, 0],
#         mode: ""
#     }, this.NIGHT_MODE_1_0_0 = {
#         id: NIGHT_MODE_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         timeStart: "",
#         timeEnd: ""
#     }, this.RE_QS_1_0_0 = {
#         id: RE_QS_DATA_ID,
#         layers: [1, 0, 0],
#         cBridgedSsid: "",
#         uWepIndex: "",
#         uSecurityType: "",
#         cPassWD: "",
#         cSsid: "",
#         cHostMac: "",
#         uPSKEncryptType: "",
#         support_mesh: "",
#         node_id: "",
#         tpie: "",
#         support_easymesh: "",
#         reserved: ""
#     }, this.RE_QS_2_0_0 = {
#         id: RE_QS_DATA_ID,
#         layers: [2, 0, 0],
#         cBridgedSsid: "",
#         uWepIndex: "",
#         uSecurityType: "",
#         cPassWD: "",
#         cSsid: "",
#         cHostMac: "",
#         uPSKEncryptType: "",
#         support_mesh: "",
#         node_id: "",
#         tpie: "",
#         support_easymesh: "",
#         reserved: ""
#     }, this.POWER_SCHEDULE_1_0_0 = {
#         id: POWER_SCHEDULE_DATA_ID,
#         layers: [1, 0, 0],
#         list: [{
#             from: "",
#             to: "",
#             repeat: "",
#             status: ""
#         }]
#     }, this.HIGH_SPEED_1_0_0 = {
#         id: HIGH_SPEED_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         configType: "",
#         mode: "",
#         linkState: "",
#         previousLink: ""
#     }, this.BLACK_LIST_1_0_0 = {
#         id: BLACK_LIST_DATA_ID,
#         layers: [1, 0, 0],
#         hList: [{
#             hName: "",
#             hDevType: "",
#             hMac: "",
#             hReserved: ""
#         }]
#     }, this.WHITE_LIST_1_0_0 = {
#         id: WHITE_LIST_DATA_ID,
#         layers: [1, 0, 0],
#         hList: [{
#             hName: "",
#             hDevType: "",
#             hMac: "",
#             hReserved: ""
#         }]
#     }, this.CLOUD_BASIC_1_0_0 = {
#         id: CLOUD_BASIC_DATA_ID,
#         layers: [1, 0, 0],
#         alias: "",
#         legality: "",
#         illegalType: "",
#         tcspStatus: ""
#     }, this.CLOUD_FW_UPGRADE_1_0_0 = {
#         id: CLOUD_FW_UPGRADE_DATA_ID,
#         layers: [1, 0, 0],
#         type: "",
#         version: "",
#         releaseDate: "",
#         releaseLog: "",
#         url: "",
#         start: "",
#         status: "",
#         progress: "",
#         title: "",
#         latestFlag: ""
#     }, this.CLOUD_OWNER_1_0_0 = {
#         id: CLOUD_OWNER_DATA_ID,
#         layers: [1, 0, 0],
#         email: "",
#         passwd: "",
#         needUnbind: ""
#     }, this.CLOUD_CURRENT_USER_CFG_1_0_0 = {
#         id: CLOUD_CURRENT_USER_CFG_DATA_ID,
#         layers: [1, 0, 0],
#         nickname: "",
#         role: "",
#         token: "",
#         eWebURL: "",
#         status: "",
#         isBinded: "",
#         logInCloud: "",
#         needReconn: ""
#     }, this.CLOUD_DDNS_1_0_0 = {
#         id: CLOUD_DDNS_DATA_ID,
#         layers: [1, 0, 0],
#         enable: "",
#         boundDomain: "",
#         tmpDomainName: "",
#         status: "",
#         list: [{
#             domainName: "",
#             regDate: "",
#             isBind: ""
#         }]
#     }, this.CLOUD_CURRENT_USER_1_0_0 = {
#         id: CLOUD_CURRENT_USER_DATA_ID,
#         layers: [1, 0, 0],
#         curUserName: "",
#         curUserPasswd: ""
#     }, this.CLOUD_SVR_CONFIG_1_0_0 = {
#         id: CLOUD_SVR_CONFIG_DATA_ID,
#         layers: [1, 0, 0],
#         cloudSefDomain: "",
#         cloudSefPort: "",
#         cloudSvrDefaultPort: "",
#         cloudDefaultSvrDomain: "",
#         cloudDefaultSvrPort: ""
#     }, this.REGION_DATA_1_0_0 = {
#         id: REGION_DATA_ID,
#         layers: [1, 0, 0],
#         index: "",
#         countryList: [{
#             countryName: "",
#             domainRegion: ""
#         }]
#     }, this.WEB_SWITCH_1_0_0 = {
#         id: WEB_SWITCH_DATA_ID,
#         layers: [1, 0, 0],
#         supportMode: "",
#         relocatePNG: "",
#         oneMesh: "",
#         easyMesh: "",
#         multiCountryCodeSwitch: ""
#     }
# }