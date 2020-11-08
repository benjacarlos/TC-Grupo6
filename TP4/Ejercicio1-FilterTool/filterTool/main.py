import os
from enum import Enum

import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from src.filterToolApplication import myFilterToolApplication


if __name__ == "__main__":

    app = QApplication([])
    myMainWindow = QMainWindow()

    #############################################
    # Se aplican estilos según CSS StyleSheet   #
    #############################################

    with open ("src/style/style.qss", "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

    #############################################

    widget = myFilterToolApplication()

    #############################################
    # Centralización de pantalla de aplicación  #
    #############################################

    qr = widget.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(centerPoint)
    widget.move(qr.topLeft())

    #############################################

    widget.setWindowTitle("Filter Tool - Grupo 6 - Teoría de Circuitos")
    widget.show()
    app.exec()