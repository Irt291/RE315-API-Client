from enum import IntEnum
from constant import listStr
from urllib.parse import unquote



class RE315SignalLevel(IntEnum):
    VERY_GOOD = 5
    GOOD = 4
    MEDIUM = 3
    BAD = 2
    VERY_BAD = 1
    NOTHING = 0



def rssiConv(rssi: int) -> RE315SignalLevel:
    if rssi > 45:
        return RE315SignalLevel.VERY_GOOD
    elif rssi > 35:
        return RE315SignalLevel.GOOD
    elif rssi > 25:
        return RE315SignalLevel.MEDIUM
    elif rssi > 15:
        return RE315SignalLevel.BAD
    elif rssi > 0:
        return RE315SignalLevel.VERY_BAD
    else:
        return RE315SignalLevel.NOTHING
    
    

def toDict(data: listStr) -> dict:
    result = {}
    for line in data:
        content = line.split()
        dataType = content[0]

        if len(content) == 1:
            result[dataType] = None
        else:
            if len(content) == 2:
                result[dataType] = int(content[1]) if content[1].isnumeric() else unquote(content[1])
            else:
                ans = [int(i) if i.isnumeric() else unquote(i) for i in content[2:]]
                ans = ans[0] if len(ans) == 1 else ans
                if result.get(dataType):
                    result[dataType].append(ans)
                else:
                    result[dataType] = [ans]
            
    return result



def parseList(data: listStr, firstEOL: tuple[str, str]):
    result = []
    for line in data:
        content = line.split()
        if len(content) < 3: continue
        dataType, idx, value = content
        idx = int(idx)
        
        if dataType == firstEOL[0]:
            if value != firstEOL[1]:
                result.append({dataType: value})
            else: continue
        
        if idx < len(result):
            result[idx][dataType] = int(value) if value.isnumeric() else unquote(value)

    return result
        