from PyQt5.QtWidgets import *
from src.ui.filterToolWindow import Ui_filterToolWindow


class myFilterToolApplication(QMainWindow, Ui_filterToolWindow):
    def __init__(self):
        super(myFilterToolApplication, self).__init__()
        self.setupUi(self)

