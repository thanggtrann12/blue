from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def alert_popup(msg_text, case):
    """This function is used to create a popup alert"""
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText(msg_text)
    msg.setWindowTitle(case)
    msg.exec_()
