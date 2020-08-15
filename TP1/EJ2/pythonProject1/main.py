from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow

from src.ui.bodePlotter import Ui_bodePlotterWindow


class myPlot(QMainWindow, Ui_bodePlotterWindow):
    def __init__(self):
        super(myPlot, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    myMainWindow = QMainWindow()
    widget = myPlot()
    widget.show()
    app.exec()

