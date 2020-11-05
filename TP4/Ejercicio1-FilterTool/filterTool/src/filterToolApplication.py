from PyQt5.QtWidgets import *
from src.ui.filterToolWindow import Ui_filterToolWindow
from scipy import signal
from scipy import signal
import matplotlib.pyplot as plt

from template import *


class myFilterToolApplication(QMainWindow, Ui_filterToolWindow):
    def __init__(self):
        super(myFilterToolApplication, self).__init__()
        self.setupUi(self)

        self.filters=[]

        self.appTemplates = []


    # Mapeo de botones interactivos y sus respectivas funciones #

        self.goStageTwoButton.clicked.connect(self.goStageTwo)
        self.returnStageOneButton.clicked.connect(self.goStageOne)
        self.acceptParametersStageOne.clicked.connect(self.stageOneGetFilterInputs)
        self.filterTypeOption.currentTextChanged.connect(self.showMoreOptions)
        self.plotTypeOptionInput.currentTextChanged.connect(self.plotGraphic)



    def showMoreOptions (self):
        if str((self.filterTypeOption.currentText())) != "Group Delay":
            self.filterParameters.setCurrentWidget(self.freqParameters)
            if str((self.filterTypeOption.currentText())) =="Low-Pass" or str((self.filterTypeOption.currentText()))=="High-Pass":
                self.hiddenWidget.setCurrentWidget(self.dontShowHidden)
            else:
                self.hiddenWidget.setCurrentWidget(self.showHiddenWidget)
        elif str((self.filterTypeOption.currentText())) == "Group Delay":
                self.filterParameters.setCurrentWidget(self.groupDelayParameters)

    # Funciones que redirigen a pantallas#
    def goStageTwo (self):
        self.stages.setCurrentWidget(self.stageTwo)

    def goStageOne (self):
        self.stages.setCurrentWidget(self.stageOne)

    # Funciones que administrar INPUTS#

    def stageOneGetFilterInputs(self):


        self.data = {
            "A_a": 0,
            "A_p": 0,
            "w_p": 0,
            "w_a_m": 0,
            "w_a": 0,
            "w_p_m": 0,
            "n": 0,  # poner valor != 0 para harcodear
            "Q_max": 0,  # poner valor != 0 para harcodear
            "d": 0  # coeficiente de desnormalización,  0<d<1   , por defecto 0
        }

        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')
        if str (self.filterTypeOption.currentText()) == "Low-Pass":
            self.filterTypeSelected=Type.LP
            if (self.approxTypeOption.currentText()) == "Legendre":
                self.filterTypeInput = Approximation.Legendre
            elif (self.approxTypeOption.currentText()) == "Cauer":
                self.filterTypeInput = Approximation.Cauer
            elif (self.approxTypeOption.currentText()) == "Gauss":
                self.filterTypeInput = Approximation.Gauss
            elif (self.approxTypeOption.currentText()) == "Butterworth":
                self.filterTypeInput = Approximation.Butterworth
            elif (self.approxTypeOption.currentText()) == "Cheby1":
                self.filterTypeInput = Approximation.Cheby1
            elif (self.approxTypeOption.currentText()) == "Cheby2":
                self.filterTypeInput = Approximation.Cheby2
            elif (self.approxTypeOption.currentText()) == "Bessel":
                self.filterTypeInput = Approximation.Bessel
            ErrorMessage = ""
            try:
                self.data["A_a"] = float (self.aaInput.text())
            except:
                ErrorMessage = ErrorMessage + "Aa must be a valid number\n"
            try:
                self.data["A_p"] = float (self.apInput.text())
            except:
                ErrorMessage = ErrorMessage + "Ap must be a valid number \n"
            try:
                self.data["w_a"] = float (self.faInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fa must be a valid number \n"
            try:
                self.data["w_p"] = float (self.fpInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fp must be a valid number \n"


        elif str(self.filterTypeOption.currentText()) == "High-Pass":
            self.filterTypeSelected = Type.HP
            if (self.approxTypeOption.currentText()) == "Legendre":
                self.filterTypeInput = Approximation.Legendre
            elif (self.approxTypeOption.currentText()) == "Cauer":
                self.filterTypeInput = Approximation.Cauer
            elif (self.approxTypeOption.currentText()) == "Gauss":
                self.filterTypeInput = Approximation.Gauss
            elif (self.approxTypeOption.currentText()) == "Butterworth":
                self.filterTypeInput = Approximation.Butterworth
            elif (self.approxTypeOption.currentText()) == "Cheby1":
                self.filterTypeInput = Approximation.Cheby1
            elif (self.approxTypeOption.currentText()) == "Cheby2":
                self.filterTypeInput = Approximation.Cheby2
            elif (self.approxTypeOption.currentText()) == "Bessel":
                self.filterTypeInput = Approximation.Bessel
            ErrorMessage = ""
            try:
                self.data["A_a"] = float(self.aaInput.text())
            except:
                ErrorMessage = ErrorMessage + "Aa must be a valid number\n"
            try:
                self.data["A_p"] = float(self.apInput.text())
            except:
                ErrorMessage = ErrorMessage + "Ap must be a valid number \n"
            try:
                self.data["w_a"] = float(self.faInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fa must be a valid number \n"
            try:
                self.data["w_p"] = float(self.fpInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fp must be a valid number \n"
        elif str(self.filterTypeOption.currentText()) == "Band-Pass":
            self.filterTypeSelected = Type.BP
            if (self.approxTypeOption.currentText()) == "Legendre":
                self.filterTypeInput = Approximation.Legendre
            elif (self.approxTypeOption.currentText()) == "Cauer":
                self.filterTypeInput = Approximation.Cauer
            elif (self.approxTypeOption.currentText()) == "Gauss":
                self.filterTypeInput = Approximation.Gauss
            elif (self.approxTypeOption.currentText()) == "Butterworth":
                self.filterTypeInput = Approximation.Butterworth
            elif (self.approxTypeOption.currentText()) == "Cheby1":
                self.filterTypeInput = Approximation.Cheby1
            elif (self.approxTypeOption.currentText()) == "Cheby2":
                self.filterTypeInput = Approximation.Cheby2
            elif (self.approxTypeOption.currentText()) == "Bessel":
                self.filterTypeInput = Approximation.Bessel
            ErrorMessage = ""
            try:
                self.data["A_a"] = float(self.aaInput.text())
            except:
                ErrorMessage = ErrorMessage + "Aa must be a valid number\n"
            try:
                self.data["A_p"] = float(self.apInput.text())
            except:
                ErrorMessage = ErrorMessage + "Ap must be a valid number \n"
            try:
                self.data["w_a"] = float(self.faInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fa must be a valid number \n"
            try:
                self.data["w_p"] = float(self.fpInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fp must be a valid number \n"
            try:
                self.data["w_a_m"] = float(self.famInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fp must be a valid number \n"
            try:
                self.data["w_p_m"] = float(self.fpmInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fp must be a valid number \n"

            print ("Estoy en BP")
        elif str(self.filterTypeOption.currentText()) == "Band-Rejection":
            print ("Estoy en BR")
        elif str(self.filterTypeOption.currentText()) == "Group Delay":
            print ("Estoy en GD")

        try:
            self.data["n"] = int (self.filterOrderInput.text())
            if self.data["n"] < 0:
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The filter order must be a valid number \n"
        try:
            self.data["d"] = float (self.denormInput.text())
            if self.data["d"] < 0 or self.data["d"] > 1:
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The Denormalization must be a valid number (0 to 1) \n"
        try:
            self.data["Q_max"] = float (self.qmaxInput.text())
        except:
            ErrorMessage = ErrorMessage + "The QMax must be a valid number \n"

        if ErrorMessage != "":
            msgWrongInput.setText(ErrorMessage)
            msgWrongInput.exec()
        else:

            print ("Aca voy a la funcion que calcula el filtro")
            self.data = {
                "A_a": 10,
                "A_p": 3,
                "w_p": 300e3,
                "w_a_m": 100e3,
                "w_a": 200e3,
                "w_p_m": 20e3,
                "n": 0,  # poner valor != 0 para harcodear
                "Q_max": 0,  # poner valor != 0 para harcodear
                "d": 1  # coeficiente de desnormalización,  0<d<1   , por defecto 0
            }
            print(self.data)
            self.appTemplates.append(template(Type.BR, Approximation.Cheby2, self.data))
            print (self.appTemplates[len(self.appTemplates)-1].data)
            print (len(self.appTemplates))


            # self.filterOption = str(self.filterTypeOption.currentText())
            #self.approxOption = str(self.approxTypeOption.currentText())
            #self.filters.append(self.defineFilter())
            #self.plotGraphic()


    # Funciones que grafican#

    def plotGraphic(self):
        myPlotGraphicType = str(self.plotTypeOptionInput.currentText())

        if myPlotGraphicType == "Magnitude":
            self.plotMagnitude()
        elif myPlotGraphicType == "Phase":
            self.plotPhase()
        elif myPlotGraphicType == "Attenuation":
            self.plotAttenuation()
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
        self.filterToolPlotTable.canvas.axes.grid(True,linestyle='-',which="both")

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

    def plotAttenuation (self):

        print (self.filters[0].thisFilter)

        self.filterToolPlotTable.canvas.axes.clear()

        self.filterToolPlotTable.canvas.axes.semilogx(self.filters[0].thisFilter.w,self.filters[0].thisFilter.magnitudeh,label = self.filters[0].label)

        self.filterToolPlotTable.canvas.axes.grid(True, linestyle='-', which="both")
        self.filterToolPlotTable.canvas.figure.tight_layout()


        self.rectangle_p = plt.Rectangle((0, -1*self.filters[0].Ap), self.filters[0].thisFilter.fc, -1*self.filters[0].Aa - 100, fc='violet', alpha=0.8)
        self.rectangle_a = plt.Rectangle((self.filters[0].Fa, -1*self.filters[0].Aa), self.filters[0].thisFilter.w_max - self.filters[0].thisFilter.fc, self.filters[0].Aa + 30, fc='violet', alpha=0.8)


        self.filterToolPlotTable.canvas.figure.gca().add_patch(self.rectangle_p)
        self.filterToolPlotTable.canvas.figure.gca().add_patch(self.rectangle_a)

        #self.filterToolPlottable.canvas.axes.legend(fancybox=True, framealpha=0.5)
        self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [Hz]")
        self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Phase [°]")
        self.filterToolPlotTable.canvas.axes.title.set_text('Frequency Response - Phase')

        self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()





    #Una vez procesado los inputs y aceptados, este metodo crea y apendea ese nuevo filtro a la lista de filtros. Lo crea convenientemente dependiendo el tipo#








