from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDesktopWidget


def IMGShow(self, image):
    """
    This function is used to show the image"""

    self.imageToShow = self.findChild(QtWidgets.QLabel, "imageToShow")
    width = self.frameGeometry().width()
    height = self.frameGeometry().height()
    self.imageToShow.setPixmap(
        QPixmap(image).scaled(width, height, Qt.KeepAspectRatio))
    self.imageToShow.setAlignment(Qt.AlignCenter)
    self.imageToShow.resize(width, height)
