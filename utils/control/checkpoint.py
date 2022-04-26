from PyQt5 import QtWidgets


def checkpoint(self, checkPointLevel):
    self.CheckPoint1 = self.findChild(QtWidgets.QLabel, "lblCheckPoint1")
    self.CheckPoint2 = self.findChild(QtWidgets.QLabel, "lblCheckPoint2")
    self.CheckPoint3 = self.findChild(QtWidgets.QLabel, "lblCheckPoint3")

    if checkPointLevel == 1:
        self.CheckPoint1.setText("Check Point 1 : ✔")
        self.CheckPoint2.setText("Check Point 2 : X")
        self.CheckPoint3.setText("Check Point 3 : X")
    if checkPointLevel == 2:
        self.CheckPoint1.setText("Check Point 1 : ✔")
        self.CheckPoint2.setText("Check Point 2 : ✔")
        self.CheckPoint3.setText("Check Point 3 : X")
    if checkPointLevel == 3:
        self.CheckPoint1.setText("Check Point 1 : ✔")
        self.CheckPoint2.setText("Check Point 2 : ✔")
        self.CheckPoint3.setText("Check Point 3 : ✔")
    if checkPointLevel == 0:
        self.CheckPoint1.setText("Check Point 1")
        self.CheckPoint2.setText("Check Point 2")
        self.CheckPoint3.setText("Check Point 3")
