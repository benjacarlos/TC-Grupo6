from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import*
import pandas as pd
import os


from PyQt5.QtWidgets import*
from PyQt5.Qt import pyqtSlot
from matplotlib.pyplot import gca

import src.package.bodeFunctions as bode
from src.ui.bodePlotter import Ui_bodePlotterWindow

class myPlot(QMainWindow, Ui_bodePlotterWindow):
    def __init__(self):
        super(myPlot, self).__init__()
        self.setupUi(self)
        self.bodes = bode.bodes()
        self.transferFunctionAction.clicked.connect(self.showTransferFunctionInput)
        self.returnTransferFunction.clicked.connect(self.returnToTransferFunction)
        self.removePlotsAction.clicked.connect(self.removePlots)
        self.saveTransferFunction.clicked.connect(self.getTransferFunctionInput)
        self.phaseUpdateLabel.clicked.connect(self.updatePhaseLabel)
        self.gainUpdateLabel.clicked.connect(self.updateGainLabel)
        self.spiceAction.clicked.connect(self.showSpiceFunctionInput)
        self.saveSpiceFunction.clicked.connect(self.getSpiceInput)
        self.returnSpiceFunction.clicked.connect(self.returnToSpiceFunction)
        self.saveCsvFunction.clicked.connect(self.getCsvInput)
        self.returnCsvFunction.clicked.connect(self.returnToCsvFunction)
        self.csvAction.clicked.connect(self.showCsvFunctionInput)
        #Contador de labels para graficos sin nombre
        self.label_num=0


    @pyqtSlot()
    def on_plot_update(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Diagrama de BODE - MAGNITUD')
        self.plotTablePhase.canvas.axes.title.set_text('Diagrama de BODE - FASE')
        ax = gca()
        ax.legend_ = None
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

        for myBode in self.bodes.bodesList:
    #        self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, label=myBode.label, loc='upper right', shadow=True, fontsize='small')
            self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, label=myBode.label)
            self.plotTableGain.canvas.axes.grid(True,which="both")
            self.plotTablePhase.canvas.axes.semilogx(myBode.w, myBode.phase, label=myBode.label)
    #        self.plotTablePhase.canvas.axes.semilogx(myBode.w, myBode.phase, label=myBode.label, loc='upper right', shadow=True, fontsize='small')
            self.plotTablePhase.canvas.axes.grid(True,which="both")


            self.plotTableGain.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
            self.plotTablePhase.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
            self.plotTablePhase.canvas.figure.tight_layout()
            self.plotTableGain.canvas.figure.tight_layout()
            self.plotTablePhase.canvas.figure.legend()
            self.plotTableGain.canvas.figure.legend()

            self.plotTablePhase.canvas.draw()
            self.plotTableGain.canvas.draw()

    def showTransferFunctionInput(self):
        self.transferFunction.setCurrentWidget(self.transferFunctionInput)

    def showSpiceFunctionInput(self):
        self.spiceFunction.setCurrentWidget(self.spiceInput)

    def showCsvFunctionInput(self):
        self.csvFunction.setCurrentWidget(self.csvInput)

    def getTransferFunctionInput(self):
        numerator = [int(x) for x in self.transferFunctionNumInput.text().split(',')]
        denominator = [int(x) for x in self.transferFunctionDenInput.text().split(',')]

        self.myBode = bode.bodeFunction("key_values", None, numerator, denominator)

        if self.transferFunctionNameInput.text() == "":
            self.myBode.label= "H($) N°" +  str(self.label_num)
            self.label_num+=1
        else:
            self.myBode.label= self.transferFunctionNameInput.text()

        self.bodes.addBodePlot(self.myBode)
        self.on_plot_update()
        self.transferFunction.setCurrentWidget(self.transferFunctionOption)
        self.transferFunctionNumInput.clear()
        self.transferFunctionDenInput.clear()
        self.transferFunctionNameInput.clear()

    def getSpiceInput(self):
        ltspice_file = QFileDialog.getOpenFileName(self, 'Open file', filter="*.txt")[0]
        if ltspice_file.endswith('.txt'):

            raw_file = open(ltspice_file, 'r')
            lines = raw_file.readlines()
            self.myBode = bode.bodeFunction("ltspice", self.bodes.plot_from_ltspice(lines), None, None)

            if self.LTSpiceNameInput.text() == "":
                self.myBode.label = os.path.splitext(os.path.basename(raw_file.name))[0]
            else:
                self.myBode.label = self.LTSpiceNameInput.text()

            self.bodes.addBodePlot(self.myBode)
            self.on_plot_update()

        else:
            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()

    def getCsvInput(self):
        csv_file = QFileDialog.getOpenFileName(self, 'Open file', filter="*.csv")[0]
        if csv_file.endswith('.csv'):

            raw_file = open(csv_file, 'r')
            data = pd.read_csv(raw_file, sep = ';')
            self.myBode = bode.bodeFunction("mesaured_values", data, None, None)

            if self.CSVNameInput.text() == "":
                self.myBode.label = os.path.splitext(os.path.basename(raw_file.name))[0]
            else:
                self.myBode.label = self.CSVNameInput.text()

            self.bodes.addBodePlot(self.myBode)
            self.on_plot_update()

        else:
            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()


    # def openLTSpiceWindow(self):
    #     ltspice_file, _ = QFileDialog.getOpenFileName(filter="*.txt")
    #     raw_file = open(ltspice_file, 'r')
    #     lines = raw_file.readlines()
    #     self.myBode = bode.bodeFunction("ltspice", self.bodes.plot_from_ltspice(lines), None, None)
    #     self.bodes.addBodePlot(self.myBode)
    #     self.on_plot_update()


    # def openCSVWindow(self):
    #     csv_file, _ = QFileDialog.getOpenFileName(filter="*.csv")
    #     raw_file = open(csv_file, 'r')
    #     data = pd.read_csv(raw_file, sep = ';')
    #     self.myBode = bode.bodeFunction("mesaured_values", data, None, None)
    #     self.bodes.addBodePlot(self.myBode)
    #     self.on_plot_update()
    #
    #     # self.window = QtWidgets.QWidget()
    #     # self.ui = Ui_CSVInput()
    #     # self.ui.setupUi(self.window)
    #     # self.window.show()

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

    def returnToTransferFunction(self):
        self.transferFunction.setCurrentWidget(self.transferFunctionOption)

    def returnToSpiceFunction(self):
        self.spiceFunction.setCurrentWidget(self.spiceOption)

    def returnToCsvFunction(self):
        self.csvFunction.setCurrentWidget(self.csvOption)


# class myCSVPopUp (QWidget, Ui_CSVInput):
#     def __init__(self):
#         super(myCSVPopUp, self).__init__()
#         self.setupUi(self)
#     def returnToCsvFunction(self):
#         self.csvFunction.setCurrentWidget(self.csvOption)


if __name__ == "__main__":
    app = QApplication([])
    myMainWindow = QMainWindow()
    widget = myPlot()
    widget.setWindowTitle("Plot Tool - Grupo 6 - Teoría de Circuitos")
    widget.show()
    app.exec()


