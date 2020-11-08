from PyQt5.QtWidgets import *
from src.ui.filterToolWindow import Ui_filterToolWindow
from scipy import signal
from scipy import signal
import matplotlib.pyplot as plt
import extra

from template import *


class myFilterToolApplication(QMainWindow, Ui_filterToolWindow):
    def __init__(self):
        super(myFilterToolApplication, self).__init__()
        self.setupUi(self)

        self.data = 0
        self.filters=[]

        self.appTemplates = []
        self.indexForTemplate = 0
        self.absAa = 0
        self.absAp = 0
        self.absFa = 0
        self.absFp = 0
        self.absFaM = 0
        self.absFpM = 0
        self.Wpm = 0
        self.Wam=0

        self.filterTypeSelected = 0
        self.currentIndex = 0

    #Mapeo de botones interactivos y sus respectivas funciones #

        self.goStageTwoButton.clicked.connect(self.goStageTwo)
        self.returnStageOneButton.clicked.connect(self.goStageOne)
        self.acceptParametersStageOne.clicked.connect(self.stageOneGetFilterInputs)
        self.filterTypeOption.currentTextChanged.connect(self.showMoreOptions)
        self.plotTypeOptionInput.currentTextChanged.connect(self.plotGraphic)
        self.plotAllCheckBox.stateChanged.connect(lambda: self.checkboxPlotAllResponse())
        self.okToRemove.clicked.connect(self.acceptToRemove)
        self.noOkToRemove.clicked.connect(self.dontAcceptToRemove)
        self.filterDesignedLabelCombo.currentTextChanged.connect(self.verityFilter)
        self.plotTypeOptionInput_2.currentTextChanged.connect(self.plotGraphicStageTwo)
        self.removeAllStageOne.clicked.connect(self.removeAll)
        self.splitInSos.stateChanged.connect(lambda: self.printSecondOrderSystems())
        self.plotAllSos.stateChanged.connect(lambda:self.plotGraphicStageTwo())
        self.editF1.clicked.connect(self.editF1Stage)
        self.editF2.clicked.connect(self.editF2Stage)
        self.editF3.clicked.connect(self.editF3Stage)
        self.editF4.clicked.connect(self.editF4Stage)
        self.editF5.clicked.connect(self.editF5Stage)
        self.acceptEditingStage.clicked.connect(self.acceptEditingStageOption)


        self.returnEditingStage.clicked.connect(self.returnEditingStageAction)

    def acceptEditingStageOption(self):
        self.numToEdit.text().lower()
        self.denToEdit.text().lower()
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

        try:
            tempNumerator = [float(x) for x in self.numToEdit.text().split(',')]
            tempDenominator = [float(x) for x in self.denToEdit.text().split(',')]
            self.appTemplates[self.currentIndex].edit_sos_tf(tempNumerator, tempDenominator, self.stageThatWillBeEdited)
            self.printSecondOrderSystems()
        except:
            msgWrongInput.setText("Something went wrong. \n Complete the numerator and denominator with , separated values")
            msgWrongInput.exec()


        # Se procesa el input para graficarlo en formato de cociente de polinomios #

        #printedNumerator = printTransferFunctionInput(self.numerator)
        #printedDenominator = printTransferFunctionInput(self.denominator)
        #self.transferFunction.setCurrentWidget(self.transferFunctionDisplay)
        #self.transferFunctionNumDisplay.setText(printedNumerator)
        #self.transferFunctionDenDisplay.setText(printedDenominator)


    def returnEditingStageAction(self):
        self.editStagePage.setCurrentWidget(self.dontShowMeEdit)


    def editF1Stage(self):
        self.editStagePage.setCurrentWidget(self.showMeEdit)
        self.stageEdited.setText("Stage 1")
        self.stageThatWillBeEdited = 0

    def editF2Stage(self):
        self.editStagePage.setCurrentWidget(self.showMeEdit)
        self.stageEdited.setText("Stage 2")
        self.stageThatWillBeEdited = 1

    def editF3Stage(self):
        self.editStagePage.setCurrentWidget(self.showMeEdit)
        self.stageEdited.setText("Stage 3")
        self.stageThatWillBeEdited = 2

    def editF4Stage(self):
        self.editStagePage.setCurrentWidget(self.showMeEdit)
        self.stageEdited.setText("Stage 4")
        self.stageThatWillBeEdited = 3

    def editF5Stage(self):
        self.editStagePage.setCurrentWidget(self.showMeEdit)
        self.stageEdited.setText("Stage 5")
        self.stageThatWillBeEdited = 4

    def removeAll (self):
        self.removeAllFilters()
        self.addNewItemToFilterList()
        self.plotGraphic()
        self.data = 0
        self.filterTypeSelected = 0
        self.Wpm = 0
        self.Wam = 0
        self.indexForTemplate = 0


    def verityFilter(self):
        if len(self.appTemplates) != 0:
            if not self.plotAllCheckBox.isChecked():
                for template in self.appTemplates:
                    if template.tag != self.filterDesignedLabelCombo.currentText():
                        template.turn_the_approx_invisible()
                    else:
                        template.turn_the_approx_visible()

            myIndex = -1
            for template in self.appTemplates:
                myIndex = myIndex + 1
                if template.tag == self.filterDesignedLabelCombo.currentText():
                    self.currentIndex = myIndex

            self.printTransferFunction(self.currentIndex)
            self.plotGraphic()


    def checkboxPlotAllResponse(self):
        if len(self.appTemplates) != 0:
            if not self.plotAllCheckBox.isChecked():
                for template in self.appTemplates:

                    if template.tag != self.filterDesignedLabelCombo.currentText():
                        template.turn_the_approx_invisible()

            else:
                for template in self.appTemplates:
                        template.turn_the_approx_visible()


        self.plotGraphic()

    def showMoreOptions (self):
        if str((self.filterTypeOption.currentText())) != "Group Delay":
            self.approxTypeOption.clear()
            elementsToBeAdded = ["Butterworth","Cauer","Cheby1","Cheby2","Legendre"]
            for myElement in elementsToBeAdded:
                self.approxTypeOption.addItem(myElement)
            self.filterParameters.setCurrentWidget(self.freqParameters)
            if str((self.filterTypeOption.currentText())) =="Low-Pass" or str((self.filterTypeOption.currentText()))=="High-Pass":
                self.hiddenWidget.setCurrentWidget(self.dontShowHidden)
            else:
                self.hiddenWidget.setCurrentWidget(self.showHiddenWidget)
        elif str((self.filterTypeOption.currentText())) == "Group Delay":
                self.filterParameters.setCurrentWidget(self.groupDelayParameters)
                self.showJustGroupDelayOptions()

    def showJustGroupDelayOptions(self):
        self.approxTypeOption.clear()
        self.approxTypeOption.addItem("Gauss")


    # Funciones que redirigen a pantallas#
    def goStageTwo (self):
        if len(self.appTemplates) != 0:
            self.stages.setCurrentWidget(self.stageTwo)
            self.plotGraphicStageTwo()
            self.printTransferFunctionStageTwo()

        else:
            msgWrongInput = QMessageBox()
            msgWrongInput.setIcon(QMessageBox.Warning)
            msgWrongInput.setWindowTitle('Error')
            msgWrongInput.setText(
                "In order to proceed to Stage 2, at least one Filter must be added to this Stage")
            msgWrongInput.exec()

    def printTransferFunctionStageTwo (self):
        numerators= []
        denominators=[]


        numToPrint = extra.printTransferFunctionInput(self.appTemplates[self.currentIndex].actual_num)
        denToPrint = extra.printTransferFunctionInput(self.appTemplates[self.currentIndex].actual_den)
        self.hsLabelNum_2.setText(numToPrint)
        self.hsLabelDen_2.setText(denToPrint)

    def plotGraphicStageTwo(self):
        myPlotGraphicType = str(self.plotTypeOptionInput_2.currentText())

        print (str(self.plotTypeOptionInput_2.currentText()))
        if myPlotGraphicType == "Magnitude":
            self.plotMagnitudeStageTwo()
        elif myPlotGraphicType == "Phase":
            self.plotPhaseStageTwo()
        elif myPlotGraphicType == "Poles and Zeros":
            self.plotZerosAndPolesStageTwo()

    def plotMagnitudeStageTwo(self):

        self.filterToolPlotTable_2.canvas.axes.clear()
        self.filterToolPlotTable_2.canvas.axes.axes.set_xlabel("Frequency [Hz]")
        self.filterToolPlotTable_2.canvas.axes.axes.set_ylabel("Gain [Db]")
        self.filterToolPlotTable_2.canvas.axes.title.set_text('Frequency Response - Amplitude')



        w, h = signal.freqs(self.appTemplates[self.currentIndex].actual_num, self.appTemplates[self.currentIndex].actual_den)

        self.filterToolPlotTable_2.canvas.axes.semilogx(w, 20 * np.log10(abs(h)), label='n')

        if self.plotAllSos.isChecked():
            hs = list()
            if self.appTemplates[self.currentIndex].should_be_att():
                for x in range(self.appTemplates[self.currentIndex].number_of_sections):  # Cargo cada den y num  en la lista
                    hs.append(signal.freqs(self.appTemplates[self.currentIndex].singularidades["sos"][x][1], self.appTemplates[self.currentIndex].singularidades["sos"][x][0]))
            else:
                for x in range(self.appTemplates[self.currentIndex].number_of_sections):  # Cargo cada num y den  en la lista
                    hs.append(signal.freqs(self.appTemplates[self.currentIndex].singularidades["sos"][x][0], self.appTemplates[self.currentIndex].singularidades["sos"][x][1]
                                           ))

            index = 1
            if self.appTemplates[self.currentIndex].number_of_sections > 1:
                h = np.multiply(hs[0][1], hs[1][1])
                while self.appTemplates[self.currentIndex].number_of_sections > index + 1:
                    h = np.multiply(h, hs[index + 1][1])
                    index += 1
            else:
                h = hs[0][1]
            # en h queda guardado el producto de todas las transferencias evaluadas en el mismo rango de frecs
            # en hs[0][0] está guardado dicho rango
            if self.appTemplates[self.currentIndex].should_be_att():
                self.filterToolPlotTable_2.canvas.axes.semilogx(hs[0][0], abs(20 * np.log10(abs(h))), label='n1', linestyle='--', color='red')
            else:
                self.filterToolPlotTable_2.canvas.axes.semilogx(hs[0][0], 20 * np.log10(abs(h)), label='n1', linestyle='--', color='red')

        self.filterToolPlotTable_2.canvas.axes.grid(True, which='both')
        self.filterToolPlotTable_2.canvas.figure.tight_layout()

        self.filterToolPlotTable_2.canvas.draw()

    def plotPhaseStageTwo(self):
        if len(self.appTemplates) != 0:

            self.filterToolPlotTable_2.canvas.axes.clear()
            self.filterToolPlotTable_2.canvas.axes.axes.set_xlabel("Frequency [Hz]")
            self.filterToolPlotTable_2.canvas.axes.axes.set_ylabel("Phase [°]")
            self.filterToolPlotTable_2.canvas.axes.title.set_text('Frequency Response - Phase')
            system = signal.TransferFunction(self.appTemplates[self.currentIndex].actual_num, self.appTemplates[self.currentIndex].actual_den)
            w,mag,phase = signal.bode(system)
            self.filterToolPlotTable_2.canvas.axes.semilogx(w, phase)



            self.filterToolPlotTable_2.canvas.axes.grid(which='both', axis='both')
            self.filterToolPlotTable_2.canvas.figure.tight_layout()
            self.filterToolPlotTable_2.canvas.draw()


    def plotZerosAndPolesStageTwo(self):
        print ("xD")


    def goStageOne (self):
        self.stages.setCurrentWidget(self.stageOne)

    # Funciones que administrar INPUTS#

    def stageOneGetFilterInputs(self):

        self.previousData = self.data
        self.previousFilterTypeSelected = self.filterTypeSelected
        self.previousWpm = self.Wpm
        self.previousWam = self.Wam


        self.data = {
            "A_a": 0,
            "A_p": 0,
            "w_p": 0,
            "w_a_m": 0,
            "w_a": 0,
            "w_p_m": 0,
            "n": 0,  # poner valor != 0 para harcodear
            "Q_max": 0,  # poner valor != 0 para harcodear
            "d": 0,  # coeficiente de desnormalización,  0<d<1   , por defecto 0
            "tau":0,
            "wrg":0,
            "tol":0,
            "n_min":0,
            "n_max":10

        }

        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        if (self.approxTypeOption.currentText()) == "Legendre":
            self.approxTypeSelected = Approximation.Legendre
        elif (self.approxTypeOption.currentText()) == "Cauer":
            self.approxTypeSelected = Approximation.Cauer
        elif (self.approxTypeOption.currentText()) == "Gauss":
            self.approxTypeSelected = Approximation.Gauss
        elif (self.approxTypeOption.currentText()) == "Butterworth":
            self.approxTypeSelected = Approximation.Butterworth
        elif (self.approxTypeOption.currentText()) == "Cheby1":
            self.approxTypeSelected = Approximation.Cheby1
        elif (self.approxTypeOption.currentText()) == "Cheby2":
            self.approxTypeSelected = Approximation.Cheby2
        elif (self.approxTypeOption.currentText()) == "Bessel":
            self.approxTypeSelected = Approximation.Bessel

        if str (self.filterTypeOption.currentText()) == "Low-Pass":
            self.filterTypeSelected=Type.LP
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
                self.Wam = float(self.famInput.text())
            except:
                ErrorMessage = ErrorMessage + "WaM must be a valid number \n"
            try:
                self.data["w_p_m"] = float(self.fpmInput.text())
                self.Wpm = float(self.fpmInput.text())
            except:
                ErrorMessage = ErrorMessage + "WpM must be a valid number \n"

            print ("Estoy en BP")
        elif str(self.filterTypeOption.currentText()) == "Band-Rejection":
            self.filterTypeSelected = Type.BR
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
                self.Wam = float(self.famInput.text())
            except:
                ErrorMessage = ErrorMessage + "WaM must be a valid number \n"
            try:
                self.data["w_p_m"] = float(self.fpmInput.text())
                self.Wpm = float(self.fpmInput.text())
            except:
                ErrorMessage = ErrorMessage + "WpM must be a valid number \n"
            print ("Estoy en BR")
        elif str(self.filterTypeOption.currentText()) == "Group Delay":
            self.filterTypeSelected = Type.LPGD
            ErrorMessage = ""
            try:
                self.data["tau"] = float(self.tauInput.text())
            except:
                ErrorMessage = ErrorMessage + "Tau must be a valid number\n"
            try:
                self.data["wrg"] = float(self.wrgInput.text())
            except:
                ErrorMessage = ErrorMessage + "Wrg must be a valid number \n"
            try:
                self.data["tol"] = float(self.tolInput.text())
            except:
                ErrorMessage = ErrorMessage + "Tol must be a valid number \n"

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
            try:
                if self.validateParametersNotChanged()==True:
                    self.appTemplates.append(template(self.filterTypeSelected, self.approxTypeSelected, self.data))
                    self.addNewItemToFilterList()


                    self.printTransferFunction(self.indexForTemplate)
                    self.indexForTemplate = (self.indexForTemplate + 1)
                    self.plotGraphic()
                else:
                    self.hiddenWarning.setCurrentWidget(self.warningNotHidden)

            except:
                msgWrongInput.setText("Sorry, but it was not possible to calculate the filter based on your parameters. \n I am not smart enough or there is no possible filter. \n Please try with different values. ")
                msgWrongInput.exec()

    def acceptToRemove (self):
        self.removeAllFilters()
        self.appTemplates.append(template(self.filterTypeSelected, self.approxTypeSelected, self.data))
        self.addNewItemToFilterList()
        self.indexForTemplate = 0
        self.printTransferFunction(self.indexForTemplate)
        self.indexForTemplate = 1
        self.plotGraphic()
        self.hiddenWarning.setCurrentWidget(self.warningIsHidden)


    def printSecondOrderSystems(self):
        if len(self.appTemplates)!=0:
            if self.splitInSos.isChecked():
                self.showPlotSos.setCurrentWidget(self.yesPlot)
                print ("NUMBER OF SECTIONS:")
                print (self.appTemplates[self.currentIndex].number_of_sections)
                for i in range (self.appTemplates[self.currentIndex].number_of_sections):
                    num,den = self.appTemplates[self.currentIndex].get_sos_data_tf(i)
                    q = str(self.appTemplates[self.currentIndex].get_sos_q(i))
                    print (num)
                    print (den)
                    numToPrint = extra.printTransferFunctionInput(num)
                    denToPrint = extra.printTransferFunctionInput(den)
                    if i == 0:
                      self.Function1.setCurrentWidget(self.F1)
                      self.f1Num.setText(numToPrint)
                      self.f1Den.setText(denToPrint)
                      self.q1.setText(q)
                    elif i ==1:
                        self.Function2.setCurrentWidget(self.F2)
                        self.f2Num.setText(numToPrint)
                        self.f2Den.setText(denToPrint)
                        self.q2.setText(q)

                    elif i == 2:
                        self.Function3.setCurrentWidget(self.F3)
                        self.f3Num.setText(numToPrint)
                        self.f3Den.setText(denToPrint)
                        self.q3.setText(q)

                    elif i == 3:
                        self.Function4.setCurrentWidget(self.F4)
                        self.f4Num.setText(numToPrint)
                        self.f4Den.setText(denToPrint)
                        self.q4.setText(q)

                    elif i == 4:
                        self.Function5.setCurrentWidget(self.F5)
                        self.f5Num.setText(numToPrint)
                        self.f5Den.setText(denToPrint)
                        self.q5.setText(q)
            else:
                self.Function1.setCurrentWidget(self.noF1)
                self.Function2.setCurrentWidget(self.noF2)
                self.Function3.setCurrentWidget(self.noF3)
                self.Function4.setCurrentWidget(self.noF4)
                self.Function5.setCurrentWidget(self.noF5)
                self.showPlotSos.setCurrentWidget(self.noPlot)




    def dontAcceptToRemove(self):
        self.data = self.previousData
        self.hiddenWarning.setCurrentWidget(self.warningNotHidden)

    def removeAllFilters(self):
        self.appTemplates.clear()

    def validateParametersNotChanged (self):

        print (self.previousData)
        print (self.data)
        print (self.previousWam)
        print (self.Wam)
        print (self.previousWpm)
        print (self.Wpm)


        goodParameters = True
        if self.indexForTemplate != 0:
            if (self.previousData["A_a"] != self.data["A_a"]) or (self.previousData["A_p"] != self.data["A_p"]) or (self.previousData["w_p"] != self.data["w_p"]) or (self.previousData["w_a"] != self.data["w_a"]) or (self.previousWam != self.Wam) or (self.previousWpm != self.Wpm) or (self.previousFilterTypeSelected != self.filterTypeSelected):
                goodParameters = False
        return goodParameters




    def printTransferFunction (self,theIndex):
        numerators= []
        denominators=[]

        numToPrint = extra.printTransferFunctionInput(self.appTemplates[theIndex].actual_num)
        denToPrint = extra.printTransferFunctionInput(self.appTemplates[theIndex].actual_den)
        self.hsLabelNum.setText(numToPrint)
        self.hsLabelDen.setText(denToPrint)




    def addNewItemToFilterList (self):


        if len(self.appTemplates)!=0:

            self.filterDesignedLabelCombo.clear()
            for line in self.appTemplates:
                self.filterDesignedLabelCombo.addItem(line.tag)

            tempIndex= len(self.appTemplates)-1
            print (tempIndex)

            self.filterDesignedLabelCombo.setCurrentText(self.appTemplates[tempIndex].tag)
        else:
            self.filterDesignedLabelCombo.clear()
            self.hsLabelNum.setText("")
            self.hsLabelDen.setText("")


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
            self.plotImpulseResponse()
        elif myPlotGraphicType == "Step Response":
            self.plotStepResponse()
        elif myPlotGraphicType == "Maximum Q":
            print("Voy a Funcion:" + myPlotGraphicType)



    def plotMagnitude (self):

        self.filterToolPlotTable.canvas.axes.clear()
        if len(self.appTemplates) != 0:
            self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [Hz]")
            self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Gain [Db]")
            self.filterToolPlotTable.canvas.axes.title.set_text('Frequency Response - Amplitude')

            for template in self.appTemplates:
                if template.should_be_drawn() == True:
                    if template.type == Type.LPN:
                        w, h = signal.freqs(template.normalized_num, template.normalized_den)
                    else:
                        w, h = signal.freqs(template.actual_num, template.actual_den)

                    self.filterToolPlotTable.canvas.axes.semilogx(w, 20 * np.log10(abs(h)), label=template.printTag)
                    self.filterToolPlotTable.canvas.axes.grid(True, which='both')
                    #self.filterToolPlotTable.canvas.axes.minoticks_on()
                    #self.filterToolPlotTable.canvas.axes.margins(0, 0.1)
                    self.filterToolPlotTable.canvas.figure.tight_layout()
                theLegend = self.filterToolPlotTable.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize = 6)

            if self.appTemplates[0].should_draw_template() and self.appTemplates[0].approximation != Approximation.Gauss:
                if self.appTemplates[0].type == Type.LP:
                    rectangle_p = plt.Rectangle((0, -self.appTemplates[0].data["A_p"]), self.appTemplates[0].data["w_p"],
                                                        -self.appTemplates[0].data["A_a"] - 100, fc='violet', alpha=0.8)
                    rectangle_a = plt.Rectangle((template.data["w_a"], -template.data["A_a"]),
                                                        1e6 - self.appTemplates[0].data["w_p"], self.appTemplates[0].data["A_a"] + 30, fc='violet',
                                                        alpha=0.8)

                if self.appTemplates[0].type == Type.LPN:
                    rectangle_p = plt.Rectangle((0, -self.appTemplates[0].data["A_p"]), 1, -self.appTemplates[0].data["A_a"] - 100,
                                                        fc='violet', alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].w_a_n, -self.appTemplates[0].data["A_a"]), 1e6 - 1,
                                                        self.appTemplates[0].data["A_a"] + 30, fc='violet', alpha=0.8)

                if self.appTemplates[0].type == Type.HP:
                    rectangle_p = plt.Rectangle((0, 0), self.appTemplates[0].data["w_a"], -self.appTemplates[0].data["A_a"], fc='violet',
                                                        alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_p"], -self.appTemplates[0].data["A_p"]),
                                                        1e6 - self.appTemplates[0].data["w_p"], -self.appTemplates[0].data["A_a"] - 200,
                                                        fc='violet', alpha=0.8)

                if self.appTemplates[0].type == Type.BP:
                    rectangle_p = plt.Rectangle((0, -self.appTemplates[0].data["A_a"]), self.appTemplates[0].data["w_a_m"],
                                                        self.appTemplates[0].data["A_a"], fc='violet', alpha=0.8)
                    rectangle_p1 = plt.Rectangle((self.appTemplates[0].data["w_a"], -self.appTemplates[0].data["A_a"]),
                                                         self.appTemplates[0].data["w_a"] + 10e6, self.appTemplates[0].data["A_a"], fc='violet',
                                                         alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_p_m"], -self.appTemplates[0].data["A_p"]), template.bw,
                                                        -self.appTemplates[0].data["A_a"] - 200, fc='violet', alpha=0.8)

                    self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_p1)


                if self.appTemplates[0].type == Type.BR:
                    rectangle_p = plt.Rectangle((0, -self.appTemplates[0].data["A_p"]), self.appTemplates[0].data["w_p_m"],
                                                        self.appTemplates[0].data["A_a"] - 300, fc='violet', alpha=0.8)
                    rectangle_p1 = plt.Rectangle((self.appTemplates[0].data["w_p"], -self.appTemplates[0].data["A_p"]),
                                                         self.appTemplates[0].data["w_a"] + 10e6, self.appTemplates[0].data["A_a"] - 300,
                                                         fc='violet', alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_a_m"], 0),
                                                        self.appTemplates[0].data["w_a"] - self.appTemplates[0].data["w_a_m"],
                                                        -self.appTemplates[0].data["A_a"], fc='violet', alpha=0.8)

                    self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_p1)

                self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_p)
                self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_a)




        self.filterToolPlotTable.canvas.draw()

    def plotAttenuation (self):

        self.filterToolPlotTable.canvas.axes.clear()
        if len(self.appTemplates) != 0:

            self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [Hz]")
            self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Gain [Db]")
            self.filterToolPlotTable.canvas.axes.title.set_text('Attenuation')

            for template in self.appTemplates:
                if template.should_be_drawn() == True:
                    if template.type == Type.LPN:
                        w, h = signal.freqs(template.normalized_den, template.normalized_num)
                    else:
                        w, h = signal.freqs(template.actual_den, template.actual_num)

                    self.filterToolPlotTable.canvas.axes.semilogx(w, 20 * np.log10(abs(h)), label=template.printTag)
                    self.filterToolPlotTable.canvas.axes.grid(True, which='both')
                    # self.filterToolPlotTable.canvas.axes.minoticks_on()
                    # self.filterToolPlotTable.canvas.axes.margins(0, 0.1)
                    self.filterToolPlotTable.canvas.figure.tight_layout()
                theLegend = self.filterToolPlotTable.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)

            if self.appTemplates[0].should_draw_template() and self.appTemplates[0].approximation != Approximation.Gauss:
                print ("HACER CUADRADITOS")
                if self.appTemplates[0].type == Type.LP:
                    print ("ESTOY EN LP")
                    rectangle_p = plt.Rectangle((0, self.appTemplates[0].data["A_p"]), self.appTemplates[0].data["w_p"],
                                                self.appTemplates[0].data["A_a"] + 100, fc='violet', alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_a"], 0),
                                                1e6 + self.appTemplates[0].data["w_p"], self.appTemplates[0].data["A_a"] , fc='violet',
                                                alpha=0.8)

                if self.appTemplates[0].type == Type.LPN:
                    rectangle_p = plt.Rectangle((0, self.appTemplates[0].data["A_p"]), 1, self.appTemplates[0].data["A_a"] + 100, fc='violet',
                                                alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].w_a_n, 0), 1e4,
                                                self.appTemplates[0].data["A_a"], fc='violet', alpha=0.8)

                if self.appTemplates[0].type == Type.HP:
                    rectangle_p = plt.Rectangle((0, 0), self.appTemplates[0].data["w_a"], self.appTemplates[0].data["A_a"], fc='violet',
                                                alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_p"], self.appTemplates[0].data["A_p"]),
                                                1e6 + self.appTemplates[0].data["w_p"], self.appTemplates[0].data["A_a"] + 200, fc='violet',
                                                alpha=0.8)

                if self.appTemplates[0].type == Type.BP:
                    rectangle_p = plt.Rectangle((0, 0), self.appTemplates[0].data["w_a_m"],
                                                self.appTemplates[0].data["A_a"], fc='violet', alpha=0.8)
                    rectangle_p1 = plt.Rectangle((self.appTemplates[0].data["w_a"], 0),
                                                 self.appTemplates[0].data["w_a"] + 10e6, self.appTemplates[0].data["A_a"], fc='violet',
                                                 alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_p_m"], self.appTemplates[0].data["A_p"]), self.appTemplates[0].bw,
                                                self.appTemplates[0].data["A_a"] + 200, fc='violet', alpha=0.8)

                    self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_p1)

                if self.appTemplates[0].type == Type.BR:
                    rectangle_p = plt.Rectangle((0, self.appTemplates[0].data["A_p"]), self.appTemplates[0].data["w_p_m"],
                                                self.appTemplates[0].data["A_a"] + 300, fc='violet', alpha=0.8)
                    rectangle_p1 = plt.Rectangle((self.appTemplates[0].data["w_p"], self.appTemplates[0].data["A_p"]),
                                                 self.appTemplates[0].data["w_a"] + 10e6, self.appTemplates[0].data["A_a"] ++ 300, fc='violet',
                                                 alpha=0.8)
                    rectangle_a = plt.Rectangle((self.appTemplates[0].data["w_a_m"], 0),
                                                self.appTemplates[0].data["w_a"] - self.appTemplates[0].data["w_a_m"], self.appTemplates[0].data["A_a"],
                                                fc='violet', alpha=0.8)

                    self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_p1)

                self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_p)
                self.filterToolPlotTable.canvas.figure.gca().add_patch(rectangle_a)

        self.filterToolPlotTable.canvas.draw()





    def plotPhase (self):

        self.filterToolPlotTable.canvas.axes.clear()
        if len(self.appTemplates) != 0:



            for template in self.appTemplates:

                if template.should_be_drawn():

                    system = signal.TransferFunction(template.actual_num, template.actual_den)

                    w,mag,phase = signal.bode(system)


                    self.filterToolPlotTable.canvas.axes.semilogx(w, phase,label=template.printTag)
                    self.filterToolPlotTable.canvas.axes.grid(True, which='both')
                    #self.filterToolPlotTable.canvas.axes.margins(0, 0.1)
                    self.filterToolPlotTable.canvas.figure.tight_layout()
                theLegend = self.filterToolPlotTable.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)

            #self.filterToolPlotTable.canvas.axes.grid(which='both', axis='both')
            self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [Hz]")
            self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Phase [°]")
            self.filterToolPlotTable.canvas.axes.title.set_text('Frequency Response - Phase')
            self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()

    def plotZerosAndPoles (self):

        self.filterToolPlotTable.canvas.axes.clear()
        if len(self.appTemplates) != 0:
            print ("POLES AND ZEROS")
            myZeros = [[], []]
            myPoles = [[], []]


            for template in self.appTemplates:
                if template.should_be_drawn():
                    for zero in template.actual_z:
                        myZeros[0].append(zero.real)
                        myZeros[1].append(zero.imag)
                    for pole in template.actual_p:
                        myPoles[0].append(pole.real)
                        myPoles[1].append(pole.imag)

            myMaxX = [max(myZeros[0], key=abs), max(myPoles[0], key=abs)]
            myMaxY = [max(myZeros[1], key=abs), max(myPoles[1], key=abs)]

            self.filterToolPlotTable.canvas.axes.clear()
            self.filterToolPlotTable.canvas.axes.set_axisbelow(True)
            self.filterToolPlotTable.canvas.axes.grid(True, linestyle='-', which="both")

            self.filterToolPlotTable.canvas.axes.scatter(myZeros[0], myZeros[1], marker="o", label="Zeros")
            self.filterToolPlotTable.canvas.axes.scatter(myPoles[0], myPoles[1], marker="x", label="Poles")

            self.filterToolPlotTable.canvas.axes.spines['left'].set_position('zero')
            self.filterToolPlotTable.canvas.axes.spines['left'].set_linewidth(1)
            self.filterToolPlotTable.canvas.axes.spines['right'].set_color('none')
            self.filterToolPlotTable.canvas.axes.spines['bottom'].set_position('zero')
            self.filterToolPlotTable.canvas.axes.spines['bottom'].set_linewidth(1)
            self.filterToolPlotTable.canvas.axes.spines['top'].set_color('none')

            self.filterToolPlotTable.canvas.axes.set_xlim(-1.2 * abs(max(myMaxX, key=abs)),
                                                          1.2 * abs(max(myMaxX, key=abs)))
            self.filterToolPlotTable.canvas.axes.set_ylim(-1.2 * abs(max(myMaxY, key=abs)),
                                                          1.2 * abs(max(myMaxY, key=abs)))
            self.filterToolPlotTable.canvas.axes.minorticks_on()

            self.filterToolPlotTable.canvas.axes.title.set_text('Zeros and Poles Diagram')

            self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()


    def plotGroupDelay (self):
        self.filterToolPlotTable.canvas.axes.clear()
        if len(self.appTemplates) != 0:



            for template in self.appTemplates:

                if template.should_be_drawn():
                    w, h = signal.freqs(template.actual_num, template.actual_den)
                    group_delay = -np.diff(np.unwrap(np.angle(h))) / np.diff(w)

                    self.filterToolPlotTable.canvas.axes.semilogx(w[1:], group_delay, label=template.printTag)
                    self.filterToolPlotTable.canvas.axes.grid(True, which='both')

                    self.filterToolPlotTable.canvas.figure.tight_layout()
                theLegend = self.filterToolPlotTable.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)

            self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Frequency [rad/s]")
            self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Group delay [s]")
            self.filterToolPlotTable.canvas.axes.title.set_text('Group Delay')
            self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()







    def plotImpulseResponse(self):
        self.filterToolPlotTable.canvas.axes.clear()

        if len(self.appTemplates) != 0:
            print ("IMPULSO")



            for template in self.appTemplates:

                if template.should_be_drawn() == True:
                    system = (template.actual_num,template.actual_den)
                    t,y = signal.impulse(system)

                    self.filterToolPlotTable.canvas.axes.plot(t, y,label=template.printTag)
                    #self.filterToolPlotTable.canvas.axes.grid(which='both', axis='both')
                    self.filterToolPlotTable.canvas.axes.margins(0, 0.1)
                    self.filterToolPlotTable.canvas.figure.tight_layout()
                theLegend = self.filterToolPlotTable.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)

            self.filterToolPlotTable.canvas.axes.grid(which='both', axis='both')
            self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Time [s]")
            self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Amplitude")
            self.filterToolPlotTable.canvas.axes.title.set_text('Impulse Response')

            self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()


    def plotStepResponse(self):

        self.filterToolPlotTable.canvas.axes.clear()
        if len(self.appTemplates) != 0:
            print ("ESCALON")



            for template in self.appTemplates:

                if template.should_be_drawn() == True:
                    lti = signal.lti(template.actual_num,template.actual_den)
                    t,y = signal.step(lti)

                    self.filterToolPlotTable.canvas.axes.plot(t, y,label=template.printTag)
                    #self.filterToolPlotTable.canvas.axes.grid(which='both', axis='both')
                    self.filterToolPlotTable.canvas.axes.margins(0, 0.1)
                    self.filterToolPlotTable.canvas.figure.tight_layout()
                theLegend = self.filterToolPlotTable.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)

            self.filterToolPlotTable.canvas.axes.grid(which='both', axis='both')
            self.filterToolPlotTable.canvas.axes.axes.set_xlabel("Time [s]")
            self.filterToolPlotTable.canvas.axes.axes.set_ylabel("Amplitude")
            self.filterToolPlotTable.canvas.axes.title.set_text('Step Response')

            self.filterToolPlotTable.canvas.figure.tight_layout()
        self.filterToolPlotTable.canvas.draw()













