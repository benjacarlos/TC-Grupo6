from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from src.ui.transferFunctionPopUp import Ui_transferFunctionInput
from src.ui.LTSpicePopUp import Ui_LTSpiceInput
from src.ui.csvPopUp import Ui_CSVInput

from PyQt5.Qt import pyqtSlot
import src.package.bodeFunctions as bode

from src.ui.bodePlotter import Ui_bodePlotterWindow

# Python Modules
from numpy import *
from random import *


class myPlot(QMainWindow, Ui_bodePlotterWindow):
    def __init__(self):
        super(myPlot, self).__init__()
        self.setupUi(self)
        self.figureGain = Figure()
        self.canvasGain = FigureCanvas(self.figureGain)
        self.axesGain = self.figureGain.add_subplot()
        canvasIndexGain = self.plotTableGain.addWidget(self.canvasGain)
        self.plotTableGain.setCurrentIndex(canvasIndexGain)
        self.figurePhase = Figure()
        self.canvasPhase = FigureCanvas(self.figurePhase)
        self.axesPhase = self.figurePhase.add_subplot()
        canvasIndexPhase = self.plotTablePhase.addWidget(self.canvasPhase)
        self.plotTablePhase.setCurrentIndex(canvasIndexPhase)

        self.transferFunctionAction.clicked.connect(self.openTransferFunctionWindow)
        self.spiceAction.clicked.connect(self.openLTSpiceWindow)
        self.csvAction.clicked.connect(self.openCSVWindow)

    @pyqtSlot()
    def on_plot_update(self):

        myBode = bode.bodeFunction([1], [1, 1])
        self.axesGain.clear()
        self.axesPhase.clear()
        self.axesGain.semilogx(myBode.w, myBode.mag)
        self.axesPhase.semilogx(myBode.w, myBode.phase)
        self.canvasGain.draw()
        self.canvasPhase.draw()

    def openTransferFunctionWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mytransferFunctionPopUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLTSpiceWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = myLTSpicePopUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCSVWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CSVInput()
        self.ui.setupUi(self.window)


class mytransferFunctionPopUp(QWidget, Ui_transferFunctionInput):
    def __init__(self):
        super(mytransferFunctionPopUp, self).__init__()
        self.setupUi(self)
        #self.inputOkAction.clicked.signal(self.dosomething)

    def dosomething(self):
        #numerator = self.trasnferNumeratorInput.text()
        #denominator = self.transferDenominatorInput.text()
        print ("hola")
        #self.setWindowTitle("HOLIS")
        #self.


class myLTSpicePopUp (QWidget, Ui_LTSpiceInput):
    def __init__(self):
        super(myLTSpicePopUp, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.signal(self.jeje)

    def jeje (self):
        print ("hola")

class myCSVPopUp (QWidget, Ui_CSVInput):
    def __init__(self):
        super(myCSVPopUp, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    myMainWindow = QMainWindow()
    widget = myPlot()
    widget.show()
    app.exec()


