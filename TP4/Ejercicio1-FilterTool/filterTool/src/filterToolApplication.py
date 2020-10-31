from PyQt5.QtWidgets import *
from src.ui.filterToolWindow import Ui_filterToolWindow
from scipy import signal
from filterDesigned import filterDesigned
from scipy import signal

class myFilterToolApplication(QMainWindow, Ui_filterToolWindow):
    def __init__(self):
        super(myFilterToolApplication, self).__init__()
        self.setupUi(self)

    # Mapeo de botones interactivos y sus respectivas funciones #

        self.goStageTwoButton.clicked.connect(self.goStageTwo)
        self.returnStageOneButton.clicked.connect(self.goStageOne)
        self.acceptParametersStageOne.clicked.connect(self.stageOneGetFilterInputs)
        self.plotTypeOptionInput.currentTextChanged.connect(self.plotGraphic)

    # Funciones que redirigen a pantallas#
    def goStageTwo (self):
        self.stages.setCurrentWidget(self.stageTwo)

    def goStageOne (self):
        self.stages.setCurrentWidget(self.stageOne)

    # Funciones que administrar INPUTS#

    def stageOneGetFilterInputs(self):

        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')
        if str (self.filterTypeOption.currentText()) == "Low-Pass":
            ErrorMessage = ""
            try:
                self.AaInputFilter = float (self.aaInput.text())
            except:
                ErrorMessage = ErrorMessage + "Aa must be a valid number\n"
            try:
                self.ApInputFilter = float (self.apInput.text())
            except:
                ErrorMessage = ErrorMessage + "Ap must be a valid number \n"
            try:
                self.FaInputFilter = float (self.faInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fa must be a valid number \n"
            try:
                self.FpInputFilter = float (self.fpInput_2.text())
            except:
                ErrorMessage = ErrorMessage + "Fp must be a valid number \n"

        elif str(self.filterTypeOption.currentText()) == "High-Pass":
            print ("Estoy en HP")
        elif str(self.filterTypeOption.currentText()) == "Band-Pass":
            print ("Estoy en BP")
        elif str(self.filterTypeOption.currentText()) == "Band-Rejection":
            print ("Estoy en BR")
        elif str(self.filterTypeOption.currentText()) == "Group Delay":
            print ("Estoy en GD")

        try:
            self.filterOrder = int (self.filterOrderInput.text())
            if self.filterOrder < 0:
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The filter order must be a valid number \n"
        try:
            self.denorm = float (self.denormInput.text())
            if self.denorm < 0 or self.denorm > 100:
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The Denormalization % must be a valid number (0 to 100) \n"
        try:
            self.maxQ = float (self.qmaxInput.text())
        except:
            ErrorMessage = ErrorMessage + "The QMax must be a valid number \n"

        if ErrorMessage != "":
            msgWrongInput.setText(ErrorMessage)
            msgWrongInput.exec()
        else:
            print ("Aca voy a la funcion que calcula el filtro")
            #self.defineFilter()
            self.plotGraphic()

        #print(self.AaInputFilter)
        #print(self.ApInputFilter)
        #print(self.FaInputFilter)
        #print(self.FpInputFilter)

    # Funciones que grafican#

    def plotGraphic(self):
        myPlotGraphicType = str(self.plotTypeOptionInput.currentText())

        if myPlotGraphicType == "Magnitude":
            self.plotMagnitude()
        elif myPlotGraphicType == "Phase":
            self.plotPhase()
        elif myPlotGraphicType == "Attenuation":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Attenuation - Normalized":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Group Delay":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Poles and Zeros":
            self.plotZerosAndPoles()
        elif myPlotGraphicType == "Impulse Response":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Step Response":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Maximum Q":
            print("Voy a Funcion:" + myPlotGraphicType)

    def plotMagnitude (self):
        print ("ploteador")
        self.numerator = [1]
        self.denominator = [1,1]
        self.system = signal.TransferFunction(self.numerator,self.denominator)
        self.w,self.mag,self.phase = signal.bode(self.system)

        self.filterToolPlotTable.canvas.axes.clear()
        self.filterToolPlotTable.canvas.axes.semilogx(self.w,self.mag)
        self.filterToolPlotTable.canvas.axes.grid(True, which="both")
        self.filterToolPlotTable.canvas.axes.minorticks_on()
        self.filterToolPlotTable.canvas.figure.tight_layout()

        self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Eje X")
        self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Eje Y")
        self.filterToolPlotTable.canvas.axes.title.set_text('Respuesta en Frecuencia - MAGNITUD')
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()

    def plotPhase (self):
        self.numerator = [1]
        self.denominator = [1,1]
        self.system = signal.TransferFunction(self.numerator,self.denominator)
        self.w,self.mag,self.phase = signal.bode(self.system)

        self.filterToolPlotTable.canvas.axes.clear()
        self.filterToolPlotTable.canvas.axes.semilogx(self.w,self.phase)
        self.filterToolPlotTable.canvas.axes.grid(True, which="both")
        self.filterToolPlotTable.canvas.axes.minorticks_on()
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Eje X")
        self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Eje Y")
        self.filterToolPlotTable.canvas.axes.title.set_text('Respuesta en Frecuencia - Fase')
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()

    def plotZerosAndPoles (self):
        self.numerator = [1,1]
        self.denominator = [1, 1,1]
        self.system = signal.TransferFunction(self.numerator, self.denominator)
        self.ZerosandPoles = self.system.to_zpk()
        print (self.ZerosandPoles)



    def defineFilter (self):
        print ("hola")
        self.myFilter = filterDesigned (self.AaInputFilter,self.ApInputFilter,self.FaInputFilter, self.FpInputFilter,str(self.filterTypeOption.currentText()),str(self.approxTypeOption.currentText()),self.filterOrder, self.maxQ, self.denorm)
