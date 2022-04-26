from jsons.jsonParse import jsonParse


def Callback(topic, msgPayload):
    jsonParse(topic, msgPayload)
