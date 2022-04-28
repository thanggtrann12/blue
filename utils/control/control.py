import json
from jsons.jsonParse import getData
from utils.setting.image import IMGShow
from PyQt5 import QtWidgets
from utils.control.checkpoint import checkpoint
lastLink = ""


def control(self):
    self.Name = self.findChild(QtWidgets.QLabel, "lblName")
    self.Pin = self.findChild(QtWidgets.QLabel, "lblPin")
    self.Size = self.findChild(QtWidgets.QLabel, "lblSize")
    global lastData, lastInfo, lastLink, mqttClient

    data = getData()
    if data != None:
        print(data)
        jsonData = json.loads(str(data).replace("'", '"'))
        if jsonData["Name"] != "":
            self.Name.setText(jsonData["Name"])
        if jsonData["Pin"] != "":
            self.Pin.setText(jsonData["Pin"])
        if jsonData["Size"] != "":
            self.Size.setText(jsonData["Size"])
        imageName = jsonData['Name']
        imageLink = "assets/images/"+imageName+".jpg"
        if lastLink != imageLink:
            IMGShow(self, imageLink)
            lastLink = imageLink


        # checkpoint(self, int(jsonData['CheckPoint']))
