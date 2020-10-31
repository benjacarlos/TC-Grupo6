from PyQt5.QtWidgets import *
from src.ui.filterToolWindow import Ui_filterToolWindow


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

    def stageOneGetFilterInputs(self):

        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')
        if str (self.filterTypeOption.currentText()) == "Low-Pass":
            ErrorMessage = ""
            try:
                self.AaInputFilter = float (self.aaInput.text())
            except:
                ErrorMessage = ErrorMessage + "Aa debe ser un número válido \n"
            try:
                self.ApInputFilter = float (self.apInput.text())
            except:
                ErrorMessage = ErrorMessage + "Ap debe ser un número válido \n"
            try:
                self.FaInputFilter = float (self.faInput.text())
            except:
                ErrorMessage = ErrorMessage + "Fa debe ser un número válido \n"
            try:
                self.FpInputFilter = float (self.fpInput_2.text())
            except:
                ErrorMessage = ErrorMessage + "Fp debe ser un número válido \n"

            if ErrorMessage != "":
                msgWrongInput.setText(ErrorMessage)
                msgWrongInput.exec()
            else:
                print ("Aca voy a la funcion que calcula el filtro")
                self.plotGraphic()

            print(self.AaInputFilter)
            print(self.ApInputFilter)
            print(self.FaInputFilter)
            print(self.FpInputFilter)

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