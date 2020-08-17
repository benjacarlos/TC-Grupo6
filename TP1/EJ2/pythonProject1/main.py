from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import*
import pandas as pd


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
        self.bodes = bode.bodes()
        self.transferFunctionAction.clicked.connect(self.showTransferFunctionInput)
        self.removePlotsAction.clicked.connect(self.removePlots)
        self.saveTransferFunction.clicked.connect(self.getTransferFunctionInput)
        self.phaseUpdateLabel.clicked.connect(self.updatePhaseLabel)
        self.gainUpdateLabel.clicked.connect(self.updateGainLabel)
        self.spiceAction.clicked.connect(self.openLTSpiceWindow)
        self.csvAction.clicked.connect(self.openCSVWindow)

    def openTransferFunctionWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = mytransferFunctionPopUp()
        self.ui.setupUi(self.window)
        self.window.show()



    @pyqtSlot()
    def on_plot_update(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Diagrama de BODE - MAGNITUD')
        self.plotTablePhase.canvas.axes.title.set_text('Diagrama de BODE - FASE')
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

        for myBode in self.bodes.bodesList:
            self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag)
            self.plotTableGain.canvas.axes.grid(True,which="both")
            self.plotTableGain.canvas.draw()
            self.plotTablePhase.canvas.axes.semilogx(myBode.w, myBode.phase)
            self.plotTablePhase.canvas.axes.grid(True,which="both")
            self.plotTablePhase.canvas.draw()

    def showTransferFunctionInput(self):
        self.transferFunction.setCurrentWidget(self.transferFunctionInput)

    def getTransferFunctionInput(self):
        numerator = [int(x) for x in self.transferFunctionNumInput.text().split(',')]
        denominator = [int(x) for x in self.transferFunctionDenInput.text().split(',')]
        self.myBode = bode.bodeFunction("key_values", None, numerator, denominator)
        self.bodes.addBodePlot(self.myBode)
        self.on_plot_update()
        self.transferFunction.setCurrentWidget(self.transferFunctionOption)

    def openLTSpiceWindow(self):
        ltspice_file, _ = QFileDialog.getOpenFileName(filter="*.txt")
        raw_file = open(ltspice_file, 'r')
        lines = raw_file.readlines()
        self.myBode = bode.bodeFunction("ltspice", self.bodes.plot_from_ltspice(lines), None, None)
        self.bodes.addBodePlot(self.myBode)
        self.on_plot_update()


    def openCSVWindow(self):
        csv_file, _ = QFileDialog.getOpenFileName(filter="*.csv")
        raw_file = open(csv_file, 'r')
        data = pd.read_csv(raw_file, sep = ';')
        self.myBode = bode.bodeFunction("mesaured_values", data, None, None)
        self.bodes.addBodePlot(self.myBode)
        self.on_plot_update()

        # self.window = QtWidgets.QWidget()
        # self.ui = Ui_CSVInput()
        # self.ui.setupUi(self.window)
        # self.window.show()

    def updateGainLabel(self):
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.xLabelInput.text())
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.yLabelInput.text())
        self.plotTableGain.canvas.draw()

    def updatePhaseLabel(self):  # Cambia el nombre del eje, corregir
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.xLabelInput.text())
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.yLabelInput.text())
        self.plotTablePhase.canvas.draw()

    def removePlots(self):
        self.bodes.bodesList.clear()
        self.on_plot_update()


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


