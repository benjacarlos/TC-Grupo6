from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*



from src.ui.transferFunctionPopUp import Ui_transferFunctionInput
from src.ui.LTSpicePopUp import Ui_LTSpiceInput
from src.ui.csvPopUp import Ui_CSVInput

from PyQt5.Qt import pyqtSlot
import src.package.bodeFunctions as bode

from src.ui.bodePlotter import Ui_bodePlotterWindow

class myPlot(QMainWindow, Ui_bodePlotterWindow):
    def __init__(self):
        super(myPlot, self).__init__()
        self.setupUi(self)
        self.transferFunctionAction.clicked.connect(self.on_plot_update)
        self.phaseUpdateLabel.clicked.connect(self.updatePhaseLabel)
        self.gainUpdateLabel.clicked.connect(self.updateGainLabel)
        self.spiceAction.clicked.connect(self.openLTSpiceWindow)
        self.csvAction.clicked.connect(self.openCSVWindow)

    def openTransferFunctionWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = mytransferFunctionPopUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLTSpiceWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = myLTSpicePopUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCSVWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_CSVInput()
        self.ui.setupUi(self.window)
        self.window.show()


    @pyqtSlot()
    def on_plot_update(self):

        myBode = bode.bodeFunction([1], [1, 1])

        self.plotTableGain.canvas.axes.clear()
        self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag)
        self.plotTableGain.canvas.axes.grid(True,which="both")
        self.plotTableGain.canvas.axes.title.set_text('Diagrama de BODE - MAGNITUD')
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.semilogx(myBode.w, myBode.phase)
        self.plotTablePhase.canvas.axes.grid(True,which="both")
        self.plotTablePhase.canvas.axes.title.set_text('Diagrama de BODE - FASE')
        self.plotTablePhase.canvas.draw()


    def updateGainLabel(self):
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.xLabelInput.text())
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.yLabelInput.text())
        self.plotTableGain.canvas.draw()

    def updatePhaseLabel(self):
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.xLabelInput.text())
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.yLabelInput.text())
        self.plotTablePhase.canvas.draw()



class mytransferFunctionPopUp(QWidget, Ui_transferFunctionInput):
    def __init__(self):
        super(mytransferFunctionPopUp, self).__init__()
        self.setupUi(self)
        self.inputOkAction.clicked.connect(lambda: self.closeWindow(self.transferFunctionInput))

    def closeWindow(self, window):
        # hide the screen on exit btn clicked
        window.hide()
        print ("hola")

class myLTSpicePopUp (QWidget, Ui_LTSpiceInput):
    def __init__(self):
        super(myLTSpicePopUp, self).__init__()
        self.setupUi(self)


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


