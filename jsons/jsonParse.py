import json
data = {
  "Name":"",
  "Pin":"",
  "Size":"",
}

lap1 = ""
lap2 = ""
lap3 = ""
endLap = ""
status = ""

def setstatus(msg):
    global status
    status = msg
    return status

def getStatus():
    global status
    return status




def setlap(numLap , time):
    global lap1, lap2, lap3, endLap
    if numLap == 1:
        lap1 = time
        return lap1
    elif numLap == 2:
        lap2 = time
        return lap2
    elif numLap == 3:
        lap3 = time
        return lap3
    elif numLap == 4:
        endLap = time
        return endLap
    
def getLap1():
    global lap1
    return lap1

def getLap2():
    global lap2
    return lap2

def getLap3():
    global lap3
    return lap3

def getEndLap():
    global endLap
    return endLap    

def jsonParse(msgPayload):
    global data
    msgJson = json.loads(msgPayload)
    data = msgJson
    return data


def getData():
    global data
    if data == "":
        return None
    else:
        return data
