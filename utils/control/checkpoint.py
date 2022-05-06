from PyQt5 import QtWidgets
from jsons.jsonParse import *

def checkpoint(self):
    self.CheckPoint1 = self.findChild(QtWidgets.QLabel, "lblCheckPoint1")
    self.CheckPoint2 = self.findChild(QtWidgets.QLabel, "lblCheckPoint2")
    self.CheckPoint3 = self.findChild(QtWidgets.QLabel, "lblCheckPoint3")
    if getStatus() == "stop":
        self.CheckPoint1.setText("Check Point 1")
        self.CheckPoint2.setText("Check Point 2")
        self.CheckPoint3.setText("Check Point 3")
    elif getStatus() == "start":
        if getLap1() != "":
            self.CheckPoint1.setText(getLap1())
        if getLap2() != "":
            self.CheckPoint2.setText(getLap2())
        if getLap3() != "":
            self.CheckPoint3.setText(getLap3())
    