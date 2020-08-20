from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import*
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


from PyQt5.QtWidgets import*
from PyQt5.Qt import pyqtSlot
from matplotlib.pyplot import gca
from enum import Enum
import src.package.bodeFunctions as bode


import src.package.signalFunctions as sr
from src.ui.bodePlotter import Ui_bodePlotterWindow



class PlottingMode(Enum):
    SingleGraph = 1
    DoubleGraph = 2


def printTransferFunctionInput(numberList):
    myNumString = ""
    unicodes = ['', '', '\u00B2', '\u00B3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    for i in range(len(numberList)):
        if (numberList[i]) > 0 and i == 0 and len(numberList) == 1:
            myNumString += (str(numberList[i]))
        elif (numberList[i]) > 0 and i == 0:
            myNumString += (str(numberList[i]) + "S" + str(unicodes[len(numberList) - i - 1]))
        elif (numberList[i] > 0) and i == (len(numberList) - 1):
            myNumString += ("+" + str(numberList[i]))
        elif (numberList[i] < 0) and i == (len(numberList) - 1):
            myNumString += ( str(numberList[i]))
        elif (numberList[i]) > 0 and i != 0:
            myNumString += ("+" + str(numberList[i]) + "S" + str(unicodes[len(numberList) - i - 1]))
        elif numberList[i] < 0:
            myNumString += (str(numberList[i]) + "S" + str(unicodes[len(numberList) - i - 1]))

    return str(myNumString)

class myPlot(QMainWindow, Ui_bodePlotterWindow):
    def __init__(self):
        super(myPlot, self).__init__()
        self.setupUi(self)
        self.bodes = bode.bodes()
        self.sgList = sr.sgList()
        self.x_gain_label=""
        self.y_gain_label=""
        self.x_phase_label=""
        self.y_phase_label=""

        self.sResponse = sr.SignalResponse()
        self.plotting_mode = PlottingMode.DoubleGraph
        self.transferFunctionAction.clicked.connect(self.showTransferFunctionInput)
        self.returnTransferFunction.clicked.connect(self.returnToTransferFunction)
        self.removePlotsAction.clicked.connect(self.removePlots)
        self.saveTransferFunction.clicked.connect(self.showValueTransferFunctionInput)
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
        self.transferFunctionCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("transferFunction"))
        self.spiceFunctionCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("spiceFunction"))
        self.csvFunctionCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("csvFunction"))
        self.signalResponseCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("signalResponse"))
        self.Same_plot_checkbox.stateChanged.connect(lambda: self.ChangePlotMode())
        self.acceptTransferFunction.clicked.connect(self.getTransferFunctionInput)
        self.returnTransferFunctionInput.clicked.connect(self.showTransferFunctionInput)

        self.signalFunctionAction.clicked.connect(self.showSignalFunctionMenu) #QStackedWidget Signals
        self.impulseSignalAction.clicked.connect(self.showImpulseSignalInput)
        self.stepSignalAction.clicked.connect(self.showStepSignalInput)
        self.sineSignalAction.clicked.connect(self.showSineSignalInput)
        self.squareSignalAction.clicked.connect(self.showSquareSignalInput)
        self.triangleSignalAction.clicked.connect(self.showTriangleSignalInput)
        self.returnSignalFunctionMenu.clicked.connect(self.returnToSignalFunction) #return buttons QStackedWidget Signals
        self.returnStepSignal.clicked.connect(self.returnToSignalFunctionMenu) 
        self.returnSineSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.returnSquareSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.returnTriangleSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.returnImpulseSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.saveSineSignal.clicked.connect(self.getSineSignalInput)    #save buttons QStackedWidget Signals
        self.saveStepSignal.clicked.connect(self.getStepSignalInput)
        self.saveSquareSignal.clicked.connect(self.getSquareSignalInput)
        self.saveTriangleSignal.clicked.connect(self.getTriangleSignalInput)
        self.saveImpulseSignal.clicked.connect(self.getImpulseSignalInput)  



    @pyqtSlot()
    def on_plot_update(self):

        if self.plotting_mode == PlottingMode.DoubleGraph:
            self.plot_double_graph()
        else:
            self.plot_single_graph()

    def plot_single_graph(self):
        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Diagrama de BODE - MAGNITUD y FASE')
        # self.plotTablePhase.canvas.axes.title.set_text('Diagrama de BODE - FASE')

        for myBode in self.bodes.bodesList:
            if myBode.bodeGraph == True:
                #        self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, label=myBode.label, loc='upper right', shadow=True, fontsize='small')
                if myBode.color ==None:
                    # Generates a rand color
                    myBode.color= self.bodes.colors_[self.bodes.color_index]
                    self.bodes.color_index += 1

                if myBode.bodeType == "csvFunction":
                    self.plotTableGain.canvas.axes.plot(myBode.w, myBode.mag, '-o', color=myBode.color, label="|"+myBode.label+"|")
                    self.plotTableGain.canvas.axes.plot(myBode.w, myBode.phase, '-o', color=myBode.color,label="Fase "+myBode.label)
                    self.plotTableGain.canvas.axes.set_xscale('log')
                else:
                    self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, color=myBode.color ,label="|"+myBode.label+"|")
                    self.plotTableGain.canvas.axes.plot(myBode.w, myBode.phase, color=myBode.color, linestyle='dashed', label="Fase "+myBode.label)

                self.plotTableGain.canvas.axes.grid(True, which="both")
                self.plotTableGain.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                self.plotTableGain.canvas.figure.tight_layout()


                # legend management
                myBode.gain_legend = self.plotTableGain.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize='small')

                # #refresh
                # self.plotTablePhase.canvas.draw()
                # self.plotTableGain.canvas.draw()
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()


    def plot_double_graph(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Diagrama de BODE - MAGNITUD')
        self.plotTablePhase.canvas.axes.title.set_text('Diagrama de BODE - FASE')


        for myBode in self.bodes.bodesList:
            if myBode.bodeGraph == True:

                if myBode.color == None:
                    # Generates a rand color
                    myBode.color = self.bodes.colors_[self.bodes.color_index]
                    self.bodes.color_index += 1
    #        self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, label=myBode.label, loc='upper right', shadow=True, fontsize='small')
                if myBode.bodeType=="csvFunction":
                   self.plotTableGain.canvas.axes.plot(myBode.w, myBode.mag, '-o', color=myBode.color, label=myBode.label)
                   self.plotTableGain.canvas.axes.set_xscale('log')
                   self.plotTablePhase.canvas.axes.plot(myBode.w, myBode.phase, '-o', color=myBode.color, label=myBode.label)
                   self.plotTablePhase.canvas.axes.set_xscale('log')
                else:
                    self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, color=myBode.color, label=myBode.label)
                    self.plotTablePhase.canvas.axes.semilogx(myBode.w, myBode.phase, color=myBode.color, label=myBode.label)

                self.plotTableGain.canvas.axes.grid(True,which="both")
                self.plotTablePhase.canvas.axes.grid(True,which="both")
                self.plotTableGain.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                self.plotTablePhase.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                self.plotTablePhase.canvas.figure.tight_layout()
                self.plotTableGain.canvas.figure.tight_layout()

                # legend management
                myBode.phase_legend = self.plotTablePhase.canvas.axes.legend(fancybox=True, framealpha=0.5)
                myBode.gain_legend = self.plotTableGain.canvas.axes.legend(fancybox=True, framealpha=0.5)


                # #refresh
                # self.plotTablePhase.canvas.draw()
                # self.plotTableGain.canvas.draw()
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTablePhase.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

    @pyqtSlot()
    def on_plotSignal_update(self, signal):

        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.clear()
        print(self.sResponse.sgl.signalList)
        self.plotTableGain.canvas.axes.title.set_text('Señal ' + signal)
        self.plotTablePhase.canvas.axes.title.set_text('Respuesta a ' + signal)
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

        #for Signal in self.sResponse.sgl.signalList:
        self.plotTableGain.canvas.axes.plot(self.sResponse.sgl.signalList[0][0], self.sResponse.sgl.signalList[0][1])
        self.plotTableGain.canvas.axes.grid(True,which="both")
        self.plotTablePhase.canvas.axes.plot(self.sResponse.sgl.signalList[0][2], self.sResponse.sgl.signalList[0][3])
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

    def showSignalFunctionMenu(self):
        self.signalResponse.setCurrentWidget(self.signalFunctionMenu)

    def showImpulseSignalInput(self):
        self.signalResponse.setCurrentWidget(self.impulseSignalInput)

    def showStepSignalInput(self):
        self.signalResponse.setCurrentWidget(self.stepSignalInput)

    def showSineSignalInput(self):
        self.signalResponse.setCurrentWidget(self.sineSignalInput)

    def showSquareSignalInput(self):
        self.signalResponse.setCurrentWidget(self.squareSignalInput)

    def showTriangleSignalInput(self):
        self.signalResponse.setCurrentWidget(self.triangleSignalInput)


    def showValueTransferFunctionInput (self):
        self.transferFunctionNumInput.text().lower()
        self.transferFunctionDenInput.text().lower()
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        if self.transferFunctionNumInput.text() == "" or self.transferFunctionDenInput.text() == "":
            msgWrongInput.setText("Complete el numerador y denominador con números separados por \" ,\" ")
            msgWrongInput.exec()
        elif self.transferFunctionNumInput.text() == "0" or self.transferFunctionDenInput.text() == "0":
            msgWrongInput.setText("No está permitido agregar solo \" 0\" ")
            msgWrongInput.exec()
        elif self.transferFunctionNumInput.text().islower() or self.transferFunctionDenInput.text().islower():
            msgWrongInput.setText("Solo están permitidos números separados por \" ,\" ")
            msgWrongInput.exec()
        else:
            self.numerator = [int(x) for x in self.transferFunctionNumInput.text().split(',')]
            self.denominator = [int(x) for x in self.transferFunctionDenInput.text().split(',')]
            self.bodes.addTransferFunction((self.numerator, self.denominator))
            printedNumerator = printTransferFunctionInput(self.numerator)
            printedDenominator = printTransferFunctionInput(self.denominator)
            self.transferFunction.setCurrentWidget(self.transferFunctionDisplay)
            self.transferFunctionNumDisplay.setText(printedNumerator)
            self.transferFunctionDenDisplay.setText(printedDenominator)

    def getTransferFunctionInput(self):
        self.myBode = bode.bodeFunction("key_values", None, self.numerator, self.denominator)
        self.myBode.w = ((self.myBode.w)/6.28138)
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
            try:
                self.myBode = bode.bodeFunction("ltspice", self.bodes.plot_from_ltspice(lines), None, None)

                if self.LTSpiceNameInput.text() == "":
                    self.myBode.label = os.path.splitext(os.path.basename(raw_file.name))[0]
                else:
                    self.myBode.label = self.LTSpiceNameInput.text()

                self.bodes.addBodePlot(self.myBode)
                self.on_plot_update()
                self.spiceFunction.setCurrentWidget(self.spiceOption)
                self.LTSpiceNameInput.clear()
            except:
                msgWrongExtention = QMessageBox()
                msgWrongExtention.setIcon(QMessageBox.Warning)
                msgWrongExtention.setWindowTitle('Error')
                msgWrongExtention.setText("El formato del archivo .csv no es válido")
                msgWrongExtention.exec()

        else:
            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()
            app.exec()

    def getCsvInput(self):
        csv_file = QFileDialog.getOpenFileName(self, 'Open file', filter="*.csv")[0]
        if csv_file.endswith('.csv'):

            raw_file = open(csv_file, 'r')
            data = pd.read_csv(raw_file, sep = ';')
            try:
                self.myBode = bode.bodeFunction("mesaured_values", data, None, None)

                if self.CSVNameInput.text() == "":
                    self.myBode.label = os.path.splitext(os.path.basename(raw_file.name))[0]
                else:
                    self.myBode.label = self.CSVNameInput.text()

                self.bodes.addBodePlot(self.myBode)
                self.on_plot_update()
                self.csvFunction.setCurrentWidget(self.csvOption)
                self.CSVNameInput.clear()

            except:
                msgWrongExtention = QMessageBox()
                msgWrongExtention.setIcon(QMessageBox.Warning)
                msgWrongExtention.setWindowTitle('Error')
                msgWrongExtention.setText("El formato del archivo .csv no es válido")
                msgWrongExtention.exec()

        else:
            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()

    def getImpulseSignalInput(self):
        pass

    def getStepSignalInput(self):
        self.amplitude = float(self.stepAmplitudeInput.value())
        self.sResponse.step(self.amplitude)
        self.on_plotSignal_update("escalón")
        self.stepAmplitudeInput.clear()

    def getSineSignalInput(self):
        self.amplitude = float(self.sineAmplitudInput.value())
        self.freq = float(self.sineFrequencyInput.value())
        self.phase = float(self.sinePhaseInput.value())
        self.DCLevel = float(self.sineDCLevelInput.value()) 
        self.sResponse.sine(self.amplitude, self.freq, self.phase, self.DCLevel)
        self.on_plotSignal_update("senoidal")
        self.sineAmplitudInput.clear()
        self.sineFrequencyInput.clear()
        self.sinePhaseInput.clear()
        self.sineDCLevelInput.clear()

    def getSquareSignalInput(self):
        self.amplitude = float(self.squareAmplitudInput.value())
        self.freq = float(self.squareFrequencyInput.value())
        self.duty = float(self.squareDutyInput.value())
        self.DClevel = float(self.squareDCLevelInput.value()) 
        self.sResponse.sine(self.amplitude, self.freq, self.duty, self.DClevel)
        self.on_plotSignal_update("cuadrada")
        self.squareAmplitudInput.clear()
        self.squareFrequencyInput.clear()
        self.squareDutyInput.clear()
        self.squareDCLevelInput.clear()

    def getTriangleSignalInput(self):
        self.amplitude = float(self.triangleAmplitudInput.value())
        self.freq = float(self.triangleFrequencyInput.value())
        self.symetry = float(self.triangleSymetryInput.value())
        self.DClevel = float(self.triangleDCLevelInput.value()) 
        self.sResponse.sine(self.amplitude, self.freq, self.duty, self.DCLevel)
        self.on_plotSignal_update("triangular")
        self.triangleAmplitudInput.clear()
        self.triangleFrequencyInput.clear()
        self.triangleSymetryInput.clear()
        self.triangleDCLevelInput.clear()


    def removeOrAddBodeTransferFunction(self,myBodeType):
        for myBode in self.bodes.bodesList:
            print (myBode.bodeType)
            if myBode.bodeType == myBodeType and myBode.bodeGraph == True:
                    myBode.bodeGraph = False
            elif myBode.bodeType == myBodeType and myBode.bodeGraph == False:
                    myBode.bodeGraph = True
        self.on_plot_update()

    def ChangePlotMode(self):

        if self.plotting_mode == PlottingMode.DoubleGraph:
            self.plotting_mode = PlottingMode.SingleGraph
            self.plotTablePhase.setVisible(False)
            self.plotTableGain.setGeometry(QtCore.QRect(280, 280, 651, 401))
            self.phaseUpdateLabel.setVisible(False)
            self.gainUpdateLabel.setGeometry(QtCore.QRect(90, 110, 61, 23))
            self.gainUpdateLabel.setText("H(jw)")
            self.on_plot_update()
        else:
            self.plotting_mode = PlottingMode.DoubleGraph
            self.plotTablePhase.setVisible(True)
            self.plotTableGain.setGeometry(QtCore.QRect(280, 30, 651, 401))
            # self.plotTablePhase.setGeometry(QtCore.QRect(280, 430, 651, 381))
            self.phaseUpdateLabel.setVisible(True)
            self.gainUpdateLabel.setGeometry(QtCore.QRect(60, 110, 61, 23))
            self.gainUpdateLabel.setText("|H(jw)|")
            self.on_plot_update()











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
        self.x_gain_label = self.xLabelInput.text()
        self.y_gain_label = self.yLabelInput.text()
        self.xLabelInput.clear()
        self.yLabelInput.clear()
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()


    def updatePhaseLabel(self):  # Cambia el nombre del eje, corregir
        self.x_phase_label = self.xLabelInput.text()
        self.y_phase_label = self.yLabelInput.text()
        self.xLabelInput.clear()
        self.yLabelInput.clear()
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTablePhase.canvas.figure.tight_layout()
        self.plotTablePhase.canvas.draw()

    def removePlots(self):
        self.bodes.bodesList.clear()
        self.bodes.transferFunctionList.clear()
        self.sResponse.sgl.signalList.clear()
        self.bodes.color_index=0
        self.on_plot_update()

    def returnToTransferFunction(self):
        self.transferFunction.setCurrentWidget(self.transferFunctionOption)

    def returnToSpiceFunction(self):
        self.spiceFunction.setCurrentWidget(self.spiceOption)

    def returnToCsvFunction(self):
        self.csvFunction.setCurrentWidget(self.csvOption)

    def returnToSignalFunction(self):
        self.signalResponse.setCurrentWidget(self.signalFunctionOption)

    def returnToSignalFunctionMenu(self):
        self.signalResponse.setCurrentWidget(self.signalFunctionMenu) 


# class myCSVPopUp (QWidget, Ui_CSVInput):
#     def __init__(self):
#         super(myCSVPopUp, self).__init__()
#         self.setupUi(self)
#     def returnToCsvFunction(self):
#         self.csvFunction.setCurrentWidget(self.csvOption)


if __name__ == "__main__":

    app = QApplication([])
    myMainWindow = QMainWindow()

    #############################################
    # Applying CSS StyleSheet                   #
    #############################################

    with open ("src/style/style.qss", "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

    #############################################

    widget = myPlot()

    #############################################
    # Window Center in the middle of the screen #
    #############################################

    qr = widget.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(centerPoint)
    widget.move(qr.topLeft())

    #############################################

    widget.setWindowTitle("Plot Tool - Grupo 6 - Teoría de Circuitos")
    widget.show()
    app.exec()


