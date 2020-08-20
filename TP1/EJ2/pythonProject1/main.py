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
import src.package.signalFunctions as sr
from src.ui.bodePlotter import Ui_bodePlotterWindow

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

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Diagrama de BODE - MAGNITUD')
        self.plotTablePhase.canvas.axes.title.set_text('Diagrama de BODE - FASE')
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

        for myBode in self.bodes.bodesList:
            if myBode.bodeGraph == True:
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

    @pyqtSlot()
    def on_plotSignal_update(self, signal, labelH):


        for mySignal in self.sgList.signalList:
            if mySignal.signalGraph == True:
                self.plotTableGain.canvas.axes.title.set_text('Señal ' + signal)
                self.plotTablePhase.canvas.axes.title.set_text('Respuesta a ' + signal)
                self.plotTableGain.canvas.axes.plot(mySignal.t, mySignal.u)
                self.plotTableGain.canvas.axes.grid(True,which="both")
                self.plotTablePhase.canvas.axes.plot(mySignal.tout, mySignal.yout, label = labelH)
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
            printedNumerator = printTransferFunctionInput(self.numerator)
            printedDenominator = printTransferFunctionInput(self.denominator)
            self.transferFunction.setCurrentWidget(self.transferFunctionDisplay)
            self.transferFunctionNumDisplay.setText(printedNumerator)
            self.transferFunctionDenDisplay.setText(printedDenominator)

    def getTransferFunctionInput(self):
        self.myBode = bode.bodeFunction("key_values", None, self.numerator, self.denominator)

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
            self.spiceFunction.setCurrentWidget(self.spiceOption)
            self.LTSpiceNameInput.clear()

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
            self.csvFunction.setCurrentWidget(self.csvOption)
            self.CSVNameInput.clear()

        else:
            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()
     

    def getImpulseSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear()        
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        self.amplitude = float(self.impulseAmplitudeInput.value())
        self.tf = int(self.impulseFinalTimeInput.value())

        aux = 0
        for myBode in self.bodes.bodesList:
            if myBode.bodeType == "transferFunction":
                aux += 1
                self.H = myBode.transferFunction
                self.mySignal = sr.SignalResponse("impulse", self.H, self.amplitude, None, None, None, None, self.tf)
                self.sgList.addSignalList(self.mySignal)
                self.on_plotSignal_update("impulso", myBode.label)

            elif (myBody.bodeType == "spiceFunction" and myBode.bodeGraph == True) or (myBody.bodeType == "csvFunction" and myBode.bodeGraph ==  True):
                self.on_plot_update()
                msgWrongInput.setText("Opción valida con H(s)\nDesactive las demás funciones")
                msgWrongInput.exec()

        if aux == 0:
            self.on_plot_update()
            msgWrongInput.setText("Introduzca una H(s)")
            msgWrongInput.exec()

        self.impulseAmplitudeInput.clear()
        self.signalResponse.setCurrentWidget(self.signalFunctionOption)

    def getStepSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear() 
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')
        
        self.amplitude = float(self.stepAmplitudeInput.value())
        self.tf = int(self.stepFinalTimeInput.value())
        aux = 0
        for myBode in self.bodes.bodesList:
            if myBode.bodeType == "transferFunction":
                aux += 1
                self.H = myBode.transferFunction
                self.mySignal = sr.SignalResponse("step", self.H, self.amplitude, None, None, None, None, self.tf)
                self.sgList.addSignalList(self.mySignal)
                self.on_plotSignal_update("señal escalón", myBode.label)

            elif (myBody.bodeType == "spiceFunction" and myBode.bodeGraph == True) or (myBody.bodeType == "csvFunction" and myBode.bodeGraph ==  True):
                self.on_plot_update()
                msgWrongInput.setText("Opción valida con H(s)\nDesactive las demás funciones")
                msgWrongInput.exec()
        if aux == 0:
            self.on_plot_update()
            msgWrongInput.setText("Introduzca una H(s)")
            msgWrongInput.exec()

        self.stepAmplitudeInput.clear()
        self.signalResponse.setCurrentWidget(self.signalFunctionOption)
      

    def getSineSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear() 
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        self.amplitude = float(self.sineAmplitudInput.value())
        self.freq = float(self.sineFrequencyInput.value())
        self.phase = float(self.sinePhaseInput.value())
        self.DClevel = float(self.sineDCLevelInput.value())
        self.tf = int(self.sineFinalTimeInput.value())
        aux = 0
        for myBode in self.bodes.bodesList:
            if myBode.bodeType == "transferFunction":
                aux += 1
                self.H = myBode.transferFunction
                self.mySignal = sr.SignalResponse("sine", self.H, self.amplitude, self.freq, self.phase, self.DClevel, None, self.tf)
                self.sgList.addSignalList(self.mySignal)
                self.on_plotSignal_update("senoidal", myBode.label)

            elif (myBody.bodeType == "spiceFunction" and myBode.bodeGraph == True) or (myBody.bodeType == "csvFunction" and myBode.bodeGraph ==  True):
                self.on_plot_update()
                msgWrongInput.setText("Opción valida con H(s)\nDesactive las demás funciones")
                msgWrongInput.exec()
        if aux == 0:
            self.on_plot_update()
            msgWrongInput.setText("Introduzca una H(s)")
            msgWrongInput.exec()

        self.sineAmplitudInput.clear()
        self.sineFrequencyInput.clear() 
        self.sinePhaseInput.clear()
        self.sineDCLevelInput.clear()
        self.signalResponse.setCurrentWidget(self.signalFunctionOption)

    def getSquareSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear()  
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        self.amplitude = float(self.squareAmplitudInput.value())
        self.freq = float(self.squareFrequencyInput.value())
        self.duty = float(self.squareDutyInput.value())
        self.DClevel = float(self.squareDCLevelInput.value()) 
        self.tf = int(self.squareFinalTimeInput.value())
        aux = 0
        for myBode in self.bodes.bodesList:
            if myBode.bodeType == "transferFunction":
                aux += 1
                self.H = myBode.transferFunction
                self.mySignal = sr.SignalResponse("square", self.H, self.amplitude, self.freq, None, self.DClevel, self.duty, self.tf)
                self.sgList.addSignalList(self.mySignal)
                self.on_plotSignal_update("señal cuadrada", myBode.label)

            elif (myBody.bodeType == "spiceFunction" and myBode.bodeGraph == True) or (myBody.bodeType == "csvFunction" and myBode.bodeGraph ==  True):
                self.on_plot_update()
                msgWrongInput.setText("Opción valida con H(s)\nDesactive las demás funciones")
                msgWrongInput.exec()
        if aux == 0:
            self.on_plot_update()
            msgWrongInput.setText("Introduzca una H(s)")
            msgWrongInput.exec()

        self.squareAmplitudInput.clear()
        self.squareFrequencyInput.clear()
        self.squareDutyInput.clear()
        self.squareDCLevelInput.clear()
        self.signalResponse.setCurrentWidget(self.signalFunctionOption)

    def getTriangleSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear() 
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        self.amplitude = float(self.triangleAmplitudInput.value())
        self.freq = float(self.triangleFrequencyInput.value())
        self.symetry = float(self.triangleSymetryInput.value())
        self.DClevel = float(self.triangleDCLevelInput.value()) 
        self.tf = int(self.triangleFinalTimeInput.value())
        aux = 0
        for myBode in self.bodes.bodesList:
            if myBode.bodeType == "transferFunction":
                aux += 1
                self.H = myBode.transferFunction
                self.mySignal = sr.SignalResponse("triangular", self.H, self.amplitude, self.freq, None, self.DClevel, self.symetry, self.tf)
                self.sgList.addSignalList(self.mySignal)
                self.on_plotSignal_update("señal triangular", myBode.label)

            elif (myBody.bodeType == "spiceFunction" and myBode.bodeGraph == True) or (myBody.bodeType == "csvFunction" and myBode.bodeGraph ==  True):
                self.on_plot_update()
                msgWrongInput.setText("Opción valida con H(s)\nDesactive las demás funciones")
                msgWrongInput.exec()
        if aux == 0:
            self.on_plot_update()
            msgWrongInput.setText("Introduzca una H(s)")
            msgWrongInput.exec()

        self.triangleAmplitudInput.clear()
        self.triangleFrequencyInput.clear()
        self.triangleSymetryInput.clear()
        self.triangleDCLevelInput.clear()
        self.signalResponse.setCurrentWidget(self.signalFunctionOption)

    def removeOrAddBodeTransferFunction(self,myBodeType):
        for myBode in self.bodes.bodesList:
            print (myBode.bodeType)
            if myBode.bodeType == myBodeType and myBode.bodeGraph == True:
                    myBode.bodeGraph = False
            elif myBode.bodeType == myBodeType and myBode.bodeGraph == False:
                    myBode.bodeGraph = True
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
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.xLabelInput.text())
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.yLabelInput.text())
        self.plotTableGain.canvas.draw()

    def updatePhaseLabel(self):  # Cambia el nombre del eje, corregir
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.xLabelInput.text())
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.yLabelInput.text())
        self.plotTablePhase.canvas.draw()

    def removePlots(self):
        self.bodes.bodesList.clear()
        self.sgList.signalList.clear()        
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


