import os
from enum import Enum

import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog

import src.package.bodeFunctions as bode
import src.package.signalFunctions as sr
import matplotlib as plt
from src.ui.bodePlotter import Ui_bodePlotterWindow


#############################################
# Funcionalidad:                            #
#                                           #
#############################################

class PlottingMode(Enum):
    SingleGraph = 1
    DoubleGraph = 2

#############################################
# Funcionalidad:                            #
# - Recibe una Lista de Numeros             #
# - Retorna un string con numeros elevados a#
# una determinada potencia segun su ubica-  #
# en la lista.                              #
#############################################

def printTransferFunctionInput(numberList):
    myNumString = ""

    # Representación en unicode para potencias de 2,3,4,5,6,7,8,9 #

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

#############################################
# Funcionalidad:                            #
# - Clase Principal de la aplicación Plot   #
#   Tool                                    #
#############################################

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
        self.y_aux_phase_label=""

        # Contador de labels para graficos sin nombre #

        self.label_num = 0
        self.plotting_mode = PlottingMode.DoubleGraph

        # Mapeo de botones interactivos y sus respectivas funciones #

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
        self.transferFunctionCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("transferFunction"))
        self.spiceFunctionCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("spiceFunction"))
        self.csvFunctionCheckBox.stateChanged.connect(lambda: self.removeOrAddBodeTransferFunction("csvFunction"))
        self.signalResponseCheckBox.stateChanged.connect(lambda: self.checkboxSignalResponse())
        self.Same_plot_checkbox.stateChanged.connect(lambda: self.ChangePlotMode())
        self.acceptTransferFunction.clicked.connect(self.getTransferFunctionInput)
        self.returnTransferFunctionInput.clicked.connect(self.showTransferFunctionInput)
        self.signalFunctionAction.clicked.connect(self.showSignalFunctionMenu) 
        self.impulseSignalAction.clicked.connect(self.showImpulseSignalInput)
        self.stepSignalAction.clicked.connect(self.showStepSignalInput)
        self.y_aux_LabelInput = QtWidgets.QLineEdit(self.centralwidget)
        self.y_aux_LabelInput.setObjectName("y_aux_LabelInput")
        self.y_aux_LabelInput.setGeometry(QtCore.QRect(135, 80, 75, 21))
        self.y_aux_LabelInput.setVisible(False)
        self.sineSignalAction.clicked.connect(self.showSineSignalInput)
        self.squareSignalAction.clicked.connect(self.showSquareSignalInput)
        self.triangleSignalAction.clicked.connect(self.showTriangleSignalInput)
        self.returnSignalFunctionMenu.clicked.connect(self.returnToSignalFunction)
        self.returnStepSignal.clicked.connect(self.returnToSignalFunctionMenu) 
        self.returnSineSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.returnSquareSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.returnTriangleSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.returnImpulseSignal.clicked.connect(self.returnToSignalFunctionMenu)
        self.saveSineSignal.clicked.connect(self.getSineSignalInput)    
        self.saveStepSignal.clicked.connect(self.getStepSignalInput)
        self.saveSquareSignal.clicked.connect(self.getSquareSignalInput)
        self.saveTriangleSignal.clicked.connect(self.getTriangleSignalInput)
        self.saveImpulseSignal.clicked.connect(self.getImpulseSignalInput)  

    #############################################
    # Funcionalidad:                            #
    # - Mapea hacia las funciones adecuadas en  #
    #   base a la elección del usuario para gra-#
    #   ficar en uno o dos plots                #
    #############################################

    @pyqtSlot()
    def on_plot_update(self):

        if self.plotting_mode == PlottingMode.DoubleGraph:
            self.plot_double_graph()
        else:
            self.plot_single_graph()

    #############################################
    # Funcionalidad:                            #
    # - Grafica todos los plots en un solo gra- #
    #  fico                                     #
    #############################################

    def plot_single_graph(self):
        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Respuesta en frecuencia - Magnitud y Fase')
        self.plotTableGain.canvas.aux_axes = self.plotTableGain.canvas.axes.twinx()



        for myBode in self.bodes.bodesList:
            if myBode.bodeGraph == True:
                if myBode.color ==None:

                    # Genera color aleatorio #

                    myBode.color= self.bodes.colors_[self.bodes.color_index]
                    self.bodes.color_index += 1

                    # Grafica apropiadamente según cada caso de Input #


                if myBode.bodeType == "csvFunction":
                    self.plotTableGain.canvas.axes.plot(myBode.w, myBode.mag, color=myBode.color, label="|"+myBode.label+"|")
                    self.plotTableGain.canvas.aux_axes.scatter(myBode.w, myBode.phase, color=myBode.color,label="Fase " + myBode.label)
                    self.plotTableGain.canvas.axes.set_xscale('log')
                else:
                    self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, color=myBode.color ,label="|"+myBode.label+"|")
                    self.plotTableGain.canvas.aux_axes.plot(myBode.w, myBode.phase, '--', color=myBode.color, label="Fase " + myBode.label)

                self.plotTableGain.canvas.axes.grid(True, which="both")
                self.plotTableGain.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                self.plotTableGain.canvas.figure.tight_layout()


                # Administración de Labels #
                myBode.phase_legend = self.plotTableGain.canvas.aux_axes.legend(fancybox=True, framealpha=0.5, loc='best', fontsize='small')
                # myBode.phase_legend_aux = self.plotTableGain.canvas.aux_axes.legend(fancybox=True, framealpha=1)
                myBode.gain_legend = self.plotTableGain.canvas.axes.legend(fancybox=True, framealpha=0.5, loc='best', fontsize='small')
                # myBode.phase_legend_aux = self.plotTableGain.canvas.aux_axes.legend(fancybox=True, framealpha=1)

        # Refresca el gráfico #

        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTableGain.canvas.aux_axes.axes.set_ylabel(self.y_aux_phase_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()


    #############################################
    # Funcionalidad:                            #
    # - Grafica todos los plots en dos graficos #
    #   Uno de magnitud y otro de fase          #
    #############################################

    def plot_double_graph(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.plotTableGain.canvas.axes.title.set_text('Respuesta en frecuencia - Magnitud')
        self.plotTablePhase.canvas.axes.title.set_text('Respuesta en frecuencia - Fase')


        for myBode in self.bodes.bodesList:
            if myBode.bodeGraph == True:

                if myBode.color == None:

                    # Genera color aleatorio #

                    myBode.color = self.bodes.colors_[self.bodes.color_index]
                    self.bodes.color_index += 1

                # Grafica apropiadamente según cada caso de Input #

                if myBode.bodeType=="csvFunction":
                   self.plotTableGain.canvas.axes.plot(myBode.w, myBode.mag, color=myBode.color, label=myBode.label)
                   self.plotTableGain.canvas.axes.set_xscale('log')
                   self.plotTablePhase.canvas.axes.plot(myBode.w, myBode.phase, color=myBode.color, label=myBode.label)
                   self.plotTablePhase.canvas.axes.set_xscale('log')
                else:
                    self.plotTableGain.canvas.axes.semilogx(myBode.w, myBode.mag, color=myBode.color, label=myBode.label)
                    self.plotTablePhase.canvas.axes.semilogx(myBode.w, myBode.phase, color=myBode.color, label=myBode.label)

                self.plotTableGain.canvas.axes.grid(True,which="both")
                self.plotTablePhase.canvas.axes.grid(True,which="both")

                locmaj = plt.ticker.LogLocator(base=10, numticks=12)
                self.plotTableGain.canvas.axes.xaxis.set_major_locator(locmaj)
                self.plotTablePhase.canvas.axes.xaxis.set_major_locator(locmaj)

                locmin = plt.ticker.LogLocator(base=10.0, subs=(0.2, 0.4, 0.6, 0.8), numticks=12)
                self.plotTableGain.canvas.axes.xaxis.set_minor_locator(locmin)
                self.plotTableGain.canvas.axes.xaxis.set_minor_formatter(plt.ticker.NullFormatter())
                # locmin = plt.ticker.LogLocator(base=10.0, subs=(0.2, 0.4, 0.6, 0.8), numticks=12)
                self.plotTablePhase.canvas.axes.xaxis.set_minor_locator(locmin)
                self.plotTablePhase.canvas.axes.xaxis.set_minor_formatter(plt.ticker.NullFormatter())

                # self.plotTableGain.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                # self.plotTablePhase.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!

                self.plotTablePhase.canvas.figure.tight_layout()
                self.plotTableGain.canvas.figure.tight_layout()

                # Administración de Labels #

                myBode.phase_legend = self.plotTablePhase.canvas.axes.legend(fancybox=True, framealpha=0.5)
                myBode.gain_legend = self.plotTableGain.canvas.axes.legend(fancybox=True, framealpha=0.5)

        # Refresca el gráfico #

        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.x_phase_label)
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.y_phase_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTablePhase.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

    #############################################
    # Funcionalidad:                            #
    # - Grafica señal y respuesta a señal de   -#
    #   funciones transferencia introducidas    #
    #############################################

    @pyqtSlot()
    def on_plotSignal_update(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()

        for mySignal in self.sgList.signalList:

            if mySignal.signalGraph == True:
                if mySignal.plotCheck == True:
                    self.plotTableGain.canvas.axes.title.set_text('Señal ' + mySignal.signalType)
                    self.plotTablePhase.canvas.axes.title.set_text('Respuesta a señal ' + mySignal.signalType)
                    self.plotTableGain.canvas.axes.plot(mySignal.t, mySignal.u, label = None)
                    self.plotTableGain.canvas.axes.grid(True,which="both")
                    self.plotTablePhase.canvas.axes.plot(mySignal.tout, mySignal.yout, color=mySignal.color, label = mySignal.labelH)
                    self.plotTablePhase.canvas.axes.grid(True,which="both")
                    self.plotTableGain.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                    self.plotTablePhase.canvas.axes.minorticks_on()  # Necesitamos esto para usar los ticks menores!
                    self.plotTablePhase.canvas.figure.tight_layout()
                    self.plotTableGain.canvas.figure.tight_layout()
                    mySignal.phase_legend = self.plotTablePhase.canvas.axes.legend(fancybox=True, framealpha=0.5)
                    mySignal.plotCheck == False


            # Refresca el gráfico #
        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTablePhase.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()
        self.plotTablePhase.canvas.draw()

    # Los siguientes métodos se utilizan para mapear PushButtons con cambios de Widgets #

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

    #########################################################################

    #############################################
    # Funcionalidad:                            #
    # - Muestra al usuario la función transfe-  #
    #   cia ingresada en formato cociente de po-#
    #   linomios                                #
    #############################################

    def showValueTransferFunctionInput (self):


        self.transferFunctionNumInput.text().lower()
        self.transferFunctionDenInput.text().lower()
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        # Se analiza que el input este en el formato num,num,num,...,n #
        # Caso contrario se muestra un mensaje de error pertinente     #

        # if self.transferFunctionNumInput.text() == "" or self.transferFunctionDenInput.text() == "":
        #     msgWrongInput.setText("Complete el numerador y denominador con números separados por \" ,\" ")
        #     msgWrongInput.exec()
        # elif self.transferFunctionNumInput.text() == "0" or self.transferFunctionDenInput.text() == "0":
        #     msgWrongInput.setText("No está permitido agregar solo \" 0\" ")
        #     msgWrongInput.exec()
        # elif (self.transferFunctionNumInput.text().islower() or self.transferFunctionDenInput.text().islower()) and ("e-" not in self.transferFunctionNumInput.text() or "e-" not in self.transferFunctionDenInput.text()):
        #     msgWrongInput.setText("Solo están permitidos números separados por \" ,\" ")
        #     msgWrongInput.exec()
        #
        # else:
        self.numerator = [float(x) for x in self.transferFunctionNumInput.text().split(',')]
        self.denominator = [float(x) for x in self.transferFunctionDenInput.text().split(',')]

            # Se procesa el input para graficarlo en formato de cociente de polinomios #

        printedNumerator = printTransferFunctionInput(self.numerator)
        printedDenominator = printTransferFunctionInput(self.denominator)
        self.transferFunction.setCurrentWidget(self.transferFunctionDisplay)
        self.transferFunctionNumDisplay.setText(printedNumerator)
        self.transferFunctionDenDisplay.setText(printedDenominator)

    #############################################
    # Funcionalidad:                            #
    # - Crea la función BODE de magnitud y fase #
    #   una vez que el input MANUAL fue validado#
    #   y grafica dicha función                 #
    #############################################

    def getTransferFunctionInput(self):

        self.myBode = bode.bodeFunction("key_values", None, self.numerator, self.denominator)

        # Paso de frecuencia a angular a frecuencia #

        self.myBode.w = ((self.myBode.w)/6.28138)

        # Se crea el label para la nueva función transferencia #

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

    #############################################
    # Funcionalidad:                            #
    # - Crea la función BODE de magnitud y fase #
    #   una vez que el input del output de SPICE#
    #   fue validado y grafica dicha función    #
    #############################################

    def getSpiceInput(self):
        ltspice_file = QFileDialog.getOpenFileName(self, 'Open file', filter="*.txt")[0]

        # Se verifica la extension correcta del archivo #

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

                # Se imprime mensaje de error en caso de que el archivo sea invalido #

                msgWrongExtention = QMessageBox()
                msgWrongExtention.setIcon(QMessageBox.Warning)
                msgWrongExtention.setWindowTitle('Error')
                msgWrongExtention.setText("El formato del archivo .txt no es válido")
                msgWrongExtention.exec()

        else:

            # Se imprime mensaje de Error si ningún archivo es ingresado #

            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()
            app.exec()

    #############################################
    # Funcionalidad:                            #
    # - Crea la función BODE de magnitud y fase #
    #   una vez que el input por archivo csv    #
    #   fue validado y grafica dicha función    #
    #############################################


    def getCsvInput(self):
        csv_file = QFileDialog.getOpenFileName(self, 'Open file', filter="*.csv")[0]

        # Se verifica la extension correcta del archivo #

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

            # Se imprime mensaje de error en caso de que el archivo sea invalido #

            except:
                msgWrongExtention = QMessageBox()
                msgWrongExtention.setIcon(QMessageBox.Warning)
                msgWrongExtention.setWindowTitle('Error')
                msgWrongExtention.setText("El formato del archivo .csv no es válido")
                msgWrongExtention.exec()

        # Se imprime mensaje de Error si ningún archivo es ingresado #

        else:
            msgWrongExtention = QMessageBox()
            msgWrongExtention.setIcon(QMessageBox.Warning)
            msgWrongExtention.setWindowTitle('Error')
            msgWrongExtention.setText("No se seleccionó ningún archivo")
            msgWrongExtention.exec()

    #############################################
    # Funcionalidad:                            #
    # - Recibe y gestiona los datos ingresados  #
    #   por el usuario para la respuesta a señal#
    #                                           #
    #############################################

        ## Respuesta a señal impulso ##

    def getImpulseSignalInput(self):

        # Se limpian inicialmente los graficos y la lista de señales #

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear()  

        # Se reciben los datos ingresados por el usuario y se pasa a la función que los gestiona #

        tf = float(self.impulseFinalTimeInput.value())
        if tf > 0.0000:
            amplitude = float(self.impulseAmplitudeInput.value())
            timeUnit = self.impulseTimeComboBox.currentText()
            self.callSignal("impulse", amplitude, None, None, None, None, tf, timeUnit, None)

        # Se limpian las casillas de ingreso de datos #

        self.impulseAmplitudeInput.setValue(0.000000)
        self.impulseFinalTimeInput.setValue(0.000000)


        ## Respuesta a señal escalón ##

    def getStepSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear()   
        tf = float(self.stepFinalTimeInput.value())
        if tf > 0.0000:
            amplitude = float(self.stepAmplitudeInput.value())
            timeUnit = self.stepTimeComboBox.currentText()
            self.callSignal("step", amplitude, None, None, None, None, tf, timeUnit, None)
        self.stepAmplitudeInput.setValue(0.000000)
        self.stepFinalTimeInput.setValue(0.000000)
   
        ## Respuesta a señal senoidal ##

    def getSineSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear() 
        tf = float(self.sineFinalTimeInput.value())
        if tf > 0.0000:
            amplitude = float(self.sineAmplitudInput.value())
            freq = float(self.sineFrequencyInput.value())
            phase = float(self.sinePhaseInput.value())
            DClevel = float(self.sineDCLevelInput.value())
            timeUnit = self.sineTimeComboBox.currentText()
            freqUnit = self.sineFreqComboBox.currentText()
            self.callSignal("sine", amplitude, freq, phase, DClevel, None, tf, timeUnit, freqUnit)
        self.sineAmplitudInput.setValue(0.000000)
        self.sineFrequencyInput.setValue(0.000000)
        self.sinePhaseInput.setValue(0.000000) 
        self.sineDCLevelInput.setValue(0.000000)
        self.sineFinalTimeInput.setValue(0.000000)

        ## Respuesta a señal cuadrada ##

    def getSquareSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear()  
        tf = float(self.squareFinalTimeInput.value())
        if tf > 0.0000:
            amplitude = float(self.squareAmplitudInput.value())
            freq = float(self.squareFrequencyInput.value())
            duty = float(self.squareDutyInput.value())
            DClevel = float(self.squareDCLevelInput.value()) 
            tf = float(self.squareFinalTimeInput.value())
            timeUnit = self.squareTimeComboBox.currentText()
            freqUnit = self.squareFreqComboBox.currentText()
            self.callSignal("square", amplitude, freq, None, DClevel, duty, tf, timeUnit, freqUnit)
        self.squareAmplitudInput.setValue(0.000000)
        self.squareFrequencyInput.setValue(0.000000)
        self.squareDutyInput.setValue(0.000000)
        self.squareDCLevelInput.setValue(0.000000)
        self.squareFinalTimeInput.setValue(0.000000)

        ## Respuesta a señal triangular ##

    def getTriangleSignalInput(self):

        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()
        self.sgList.signalList.clear() 
        tf = float(self.triangleFinalTimeInput.value())
        if tf > 0.0000:
            amplitude = float(self.triangleAmplitudInput.value())
            freq = float(self.triangleFrequencyInput.value())
            symetry = float(self.triangleSymetryInput.value())
            DClevel = float(self.triangleDCLevelInput.value()) 
            timeUnit = self.triangleTimeComboBox.currentText()
            freqUnit = self.triangleFreqComboBox.currentText()
            self.callSignal("triangle", amplitude, freq, None, DClevel, symetry, tf, timeUnit, freqUnit)
        self.triangleAmplitudInput.setValue(0.000000)
        self.triangleFrequencyInput.setValue(0.000000)
        self.triangleSymetryInput.setValue(0.000000)
        self.triangleDCLevelInput.setValue(0.000000)
        self.triangleFinalTimeInput.setValue(0.000000)

    #############################################
    # Funcionalidad:                            #
    # - Valida los datos ingresados, envía      #
    #   mensajes de error y crea las instancias #
    #   para los graficos de señales.           #
    #############################################

    def callSignal(self, mode, amp, freq, phase, DClevel, DutyOrSym, tf, timeUnit, freqUnit):

        # Se prepara ventana de eror #
      
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')
        auxTransferCont = 0

        # Valida la función de transferencia y pasa los datos ingresados #

        for myBode in self.bodes.bodesList:

            if myBode.bodeType == "transferFunction":
                
               # Se exige la condición que el grado del denominador sea mayor # 
               # o igual al numerador. Sino, se envía mensaje de error        #      
                if len(myBode.transferDenominator) < len(myBode.transferNumerator):
                    msgWrongInput.setText("Error: grado de numerador mayor a denominador")
                    msgWrongInput.exec()
                    self.on_plot_update()
                    aux = 1
                    break

                # De ser válida la H(s), se pasan los parámetros para el cálculo de la señal y se la grafica #

                auxTransferCont += 1
                H = myBode.transferFunction
                self.mySignal = sr.SignalResponse(mode, H, amp, freq, phase, DClevel, DutyOrSym, tf, myBode.label, timeUnit, freqUnit)
                self.sgList.addSignalList(self.mySignal)
                self.on_plotSignal_update()

            # En caso de haberse introducido un archivo de LTSpice o medición, se envía mensaje de error #

            elif (myBode.bodeType == "spiceFunction" and myBode.bodeGraph == True) or (myBode.bodeType == "csvFunction" and myBode.bodeGraph ==  True):
                msgWrongInput.setText("Opción valida con H(s)\nDesactive las demás funciones")
                msgWrongInput.exec()
                self.on_plot_update()

        #De no haberse introducido función transferencia, se envía mensaje de error#

        if auxTransferCont == 0:
            msgWrongInput.setText("Introduzca una H(s)")
            msgWrongInput.exec()
            self.on_plot_update()

    #############################################
    # Funcionalidad:                            #
    # - Activa y desactiva gráfico al presionar #
    #   el checkbox de señales.                 #
    #############################################

    def checkboxSignalResponse(self):
        
        self.plotTableGain.canvas.axes.clear()
        self.plotTablePhase.canvas.axes.clear()

        #Muestra o elimina cada uno de los gráficos de señales#

        for mySignal in self.sgList.signalList:
            if mySignal.signalGraph == True:
                mySignal.signalGraph = False
                self.on_plot_update()
            elif mySignal.signalGraph == False:
                mySignal.signalGraph = True
                mySignal.plotCheck = True 
                self.on_plotSignal_update()


    #############################################
    # Funcionalidad:                            #
    # - Setea si una funcion debe ser graficada #
    #   o no según lo que el usuario haya che-  #
    #   ado por TIPO de input                   #
    #############################################

    def removeOrAddBodeTransferFunction(self,myBodeType):

        # Se recorren los elementos BODES y se togglea su estado #

        for myBode in self.bodes.bodesList:
            if myBode.bodeType == myBodeType and myBode.bodeGraph == True:
                    myBode.bodeGraph = False
            elif myBode.bodeType == myBodeType and myBode.bodeGraph == False:
                    myBode.bodeGraph = True
        self.on_plot_update()

    #############################################
    # Funcionalidad:                            #
    # - Realiza las acciones necesarias para    #
    #   ficar apropiadamente en uno o dos gráfi-#
    #   cos.                                    #
    #############################################

    def ChangePlotMode(self):

        if self.plotting_mode == PlottingMode.DoubleGraph:
            self.plotting_mode = PlottingMode.SingleGraph
            self.plotTablePhase.setVisible(False)
            self.plotTableGain.setGeometry(QtCore.QRect(290, 280, 721, 401))
            self.phaseUpdateLabel.setVisible(False)
            self.gainUpdateLabel.setGeometry(QtCore.QRect(90, 110, 61, 23))
            self.gainUpdateLabel.setText("H(jw)")

            self.y_aux_LabelInput.setVisible(True)
            self.yLabelInput.setGeometry(QtCore.QRect(40, 80, 75, 21))

            self.on_plot_update()



        else:
            self.plotting_mode = PlottingMode.DoubleGraph
            self.plotTableGain.canvas.aux_axes.axis('off')
            self.plotTableGain.canvas.aux_axes.clear
            self.plotTableGain.canvas.aux_axes.remove()
            self.plotTablePhase.setVisible(True)
            self.plotTableGain.setGeometry(QtCore.QRect(290, 20, 721, 401))
            self.phaseUpdateLabel.setVisible(True)
            self.gainUpdateLabel.setGeometry(QtCore.QRect(60, 110, 61, 23))
            self.gainUpdateLabel.setText("|H(jw)|")
            self.y_aux_LabelInput.setVisible(False)
            self.yLabelInput.setGeometry(QtCore.QRect(40, 80, 171, 21))
            self.on_plot_update()

    #############################################
    # Funcionalidad:                            #
    # - Actualizar el valor de los labels de X  #
    #   e Y según el input del usuario para grá-#
    #   fico de MAGNITUD                        #
    #############################################

    def updateGainLabel(self):
        self.x_gain_label = self.xLabelInput.text()
        self.y_gain_label = self.yLabelInput.text()
        self.xLabelInput.clear()
        self.yLabelInput.clear()

        if self.plotting_mode==PlottingMode.SingleGraph:
            self.y_aux_phase_label = self.y_aux_LabelInput.text()
            self.y_aux_LabelInput.clear()
            self.plotTableGain.canvas.aux_axes.axes.set_ylabel(self.y_aux_phase_label)

        self.plotTableGain.canvas.axes.axes.set_xlabel(self.x_gain_label)
        self.plotTableGain.canvas.axes.axes.set_ylabel(self.y_gain_label)
        self.plotTableGain.canvas.figure.tight_layout()
        self.plotTableGain.canvas.draw()

    #############################################
    # Funcionalidad:                            #
    # - Actualizar el valor de los labels de X  #
    #   e Y según el input del usuario para grá-#
    #   fico de FASE                            #
    #############################################

    def updatePhaseLabel(self):
        self.x_phase_label = self.xLabelInput.text()
        self.y_phase_label = self.yLabelInput.text()
        self.xLabelInput.clear()
        self.yLabelInput.clear()
        self.plotTablePhase.canvas.axes.axes.set_xlabel(self.x_phase_label)
        self.plotTablePhase.canvas.axes.axes.set_ylabel(self.y_phase_label)
        self.plotTablePhase.canvas.figure.tight_layout()
        self.plotTablePhase.canvas.draw()

    #############################################
    # Funcionalidad:                            #
    # - Remover todos los gráficos ingresados   #
    #   Todos los inputs son eliminados         #
    #############################################

    def removePlots(self):
        if self.plotting_mode == PlottingMode.SingleGraph:
            self.plotTableGain.canvas.aux_axes.axis('off')
            self.plotTableGain.canvas.aux_axes.clear
            self.plotTableGain.canvas.aux_axes.remove()


        self.bodes.bodesList.clear()
        self.sgList.signalList.clear()        
        self.bodes.color_index=0
        self.on_plot_update()



#############################################
# Funcionalidad:                            #
# - Definición de Main con inicialización de#
#   la aplicación                           #
#############################################

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

    widget = myPlot()

    #############################################
    # Centralización de pantalla de aplicación  #
    #############################################

    qr = widget.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(centerPoint)
    widget.move(qr.topLeft())

    #############################################

    widget.setWindowTitle("Plot Tool - Grupo 6 - Teoría de Circuitos")
    widget.show()
    app.exec()


