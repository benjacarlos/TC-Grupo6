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
            self.plotGroupDelay()
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
        self.filterToolPlotTable.canvas.axes.grid(True,linestyle='-', which="both")
        self.filterToolPlotTable.canvas.axes.minorticks_on()
        self.filterToolPlotTable.canvas.figure.tight_layout()

        self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [Hz]")
        self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Gain [DB]")
        self.filterToolPlotTable.canvas.axes.title.set_text('Frequency Response - Amplitude')
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()

    def plotPhase (self):
        self.numerator = [1]
        self.denominator = [1,1]
        self.system = signal.TransferFunction(self.numerator,self.denominator)
        self.w,self.mag,self.phase = signal.bode(self.system)


        self.filterToolPlotTable.canvas.axes.clear()
        self.filterToolPlotTable.canvas.axes.semilogx(self.w,self.phase)
        self.filterToolPlotTable.canvas.axes.grid(True,linestyle='-', which="both")
        self.filterToolPlotTable.canvas.axes.minorticks_on()
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [Hz]")
        self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Phase [°]")
        self.filterToolPlotTable.canvas.axes.title.set_text('Frequency Response - Phase')
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()

    def plotZerosAndPoles (self):
        self.numerator = [1,1]
        self.denominator = [1, 1,1]
        self.system = signal.TransferFunction(self.numerator, self.denominator)
        print(self.system.zeros)
        print(self.system.poles)
        myZeros=[[],[]]
        myPoles= [[],[]]
        for zero in self.system.zeros:
            myZeros[0].append(zero.real)
            myZeros[1].append(zero.imag)
        for pole in self.system.poles:
            myPoles[0].append(pole.real)
            myPoles[1].append(pole.imag)
        myMaxX = [max(myZeros[0],key=abs),max(myPoles[0],key=abs)]
        myMaxY = [max(myZeros[1],key=abs),max(myPoles[1],key=abs)]

        print (max(myMaxX,key=abs))
        print (max(myMaxY, key=abs))

        self.filterToolPlotTable.canvas.axes.clear()
        self.filterToolPlotTable.canvas.axes.set_axisbelow(True)
        self.filterToolPlotTable.canvas.axes.grid(True,linestyle='-.',which="both")

        self.filterToolPlotTable.canvas.axes.scatter(myZeros[0],myZeros[1],marker="o",label="Zeros")
        self.filterToolPlotTable.canvas.axes.scatter(myPoles[0],myPoles[1],marker="x",label = "Poles")

        self.filterToolPlotTable.canvas.axes.spines['left'].set_position('zero')
        self.filterToolPlotTable.canvas.axes.spines['left'].set_linewidth(1)
        self.filterToolPlotTable.canvas.axes.spines['right'].set_color('none')
        self.filterToolPlotTable.canvas.axes.spines['bottom'].set_position('zero')
        self.filterToolPlotTable.canvas.axes.spines['bottom'].set_linewidth(1)
        self.filterToolPlotTable.canvas.axes.spines['top'].set_color('none')

        self.filterToolPlotTable.canvas.axes.set_xlim(-1.2*abs(max(myMaxX,key=abs)),1.2*abs(max(myMaxX,key=abs)))
        self.filterToolPlotTable.canvas.axes.set_ylim(-1.2 * abs(max(myMaxY, key=abs)), 1.2 * abs(max(myMaxY, key=abs)))
        self.filterToolPlotTable.canvas.axes.minorticks_on()

        self.filterToolPlotTable.canvas.axes.title.set_text('Zeros and Poles Diagram')

        #self.filterToolPlotTablecanvas.axes.legend(fancybox=True, framealpha=0.5)
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()


    def plotGroupDelay (self):
        self.numerator = [1]
        self.denominator = [10000,23123123]
        self.system = signal.TransferFunction(self.numerator,self.denominator)
        self.w,self.gd= signal.group_delay((self.numerator,self.denominator))
        self.filterToolPlotTable.canvas.axes.clear()
        self.filterToolPlotTable.canvas.axes.plot(self.w,self.gd)
        self.filterToolPlotTable.canvas.axes.grid(True,linestyle='-', which="both")
        self.filterToolPlotTable.canvas.axes.minorticks_on()
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [rad/sample]")
        self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Group delay [samples]")
        self.filterToolPlotTable.canvas.axes.title.set_text('Group Delay')
        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()

    def defineFilter (self):
        print ("hola")
        self.myFilter = filterDesigned (self.AaInputFilter,self.ApInputFilter,self.FaInputFilter, self.FpInputFilter,str(self.filterTypeOption.currentText()),str(self.approxTypeOption.currentText()),self.filterOrder, self.maxQ, self.denorm)
