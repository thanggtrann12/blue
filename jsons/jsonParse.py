import json
data = {
  "Name":"",
  "Pin":"",
  "Size":"",
}


def jsonParse(msgPayload):
    global data
    msgJson = json.loads(msgPayload)
    data = msgJson
    print(data)
    return data


def getData():
    global data
    if data == "":
        return None
    else:
        return data
