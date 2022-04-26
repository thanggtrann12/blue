import json
from jsons.jsonParse import getData
from mqtt.functions.callback import Callback
from mqtt.functions.getinfo import subscribe
from mqtt.functions.teaminfo import getInfo
from mqtt.client.client import connect_mqtt
from utils.setting.image import IMGShow
from PyQt5 import QtWidgets
from utils.control.checkpoint import checkpoint
lastData = ""
lastInfo = ""
lastLink = ""


def cleanData(data):
    data = str(data)
    firstIndex = data.find('{')
    lastIndex = data.find('}')
    data = data[firstIndex:lastIndex+1]
    print(data)
    return str(data)


mqttClient = connect_mqtt(Callback)


def control(self):
    self.Name = self.findChild(QtWidgets.QLabel, "lblName")
    self.Pin = self.findChild(QtWidgets.QLabel, "lblPin")
    self.Size = self.findChild(QtWidgets.QLabel, "lblSize")
    global lastData, lastInfo, lastLink

    data = getData()
    if data != None:
        jsonData = json.loads(str(data).replace("'", '"'))
        subscribe(jsonData['Code'])
        info = getInfo()
        if info != None:
            jsonInfo = json.loads(info.decode())
            self.Name.setText(jsonInfo['Name'])
            self.Pin.setText(jsonInfo['Pin'])
            self.Size.setText(jsonInfo['Size'])
            imageName = jsonInfo['Name']
            imageLink = "assets/images/"+imageName+".jpg"
            if lastLink != imageLink:
                IMGShow(self, imageLink)
                lastLink = imageLink

        checkpoint(self, int(jsonData['CheckPoint']))
