from PyQt5.QtWidgets import *
from src.ui.filterToolWindow import Ui_filterToolWindow
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
            self.plotGraphic()

        #print(self.AaInputFilter)
        #print(self.ApInputFilter)
        #print(self.FaInputFilter)
        #print(self.FpInputFilter)

    # Funciones que grafican#

    def plotGraphic(self):
        myPlotGraphicType = str(self.plotTypeOptionInput.currentText())

        if myPlotGraphicType == "Magnitude":
            print ("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Phase":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Attenuation":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Attenuation - Normalized":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Group Delay":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Poles and Zeros":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Impulse Response":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Step Response":
            print("Voy a Funcion:" + myPlotGraphicType)
        elif myPlotGraphicType == "Maximum Q":
            print("Voy a Funcion:" + myPlotGraphicType)

#control.pzmap(sys, Plot=True, title='Pole Zero Map')
#Plot a pole/zero map for a linear system.

#Parameters:
#sys (LTI (StateSpace or TransferFunction)) – Linear system for which poles and zeros are computed.
#Plot (bool) – If True a graph is generated with Matplotlib, otherwise the poles and zeros are only computed and returned.
#Returns:
#pole (array) – The systems poles
#zeros (array) – The system’s zeros.


