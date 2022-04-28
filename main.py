from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDesktopWidget
import sys
from mqtt.client.client import Create_connections
from utils.control.control import control
from utils.setting.wireless import check_ping
from mqtt.functions.msgPopUp import alert_popup

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("Ui/main.ui", self)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        if check_ping():
          Create_connections()
        else:
          alert_popup("No internet connection", "Error")
        timer = QTimer(self)
        timer.timeout.connect(lambda: control(self))
        timer.start(1000)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
