# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\bodePlotter.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bodePlotterWindow(object):
    def setupUi(self, bodePlotterWindow):
        bodePlotterWindow.setObjectName("bodePlotterWindow")
        bodePlotterWindow.resize(1165, 915)
        self.centralwidget = QtWidgets.QWidget(bodePlotterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xLabelText = QtWidgets.QLabel(self.centralwidget)
        self.xLabelText.setGeometry(QtCore.QRect(60, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.xLabelText.setFont(font)
        self.xLabelText.setObjectName("xLabelText")
        self.yLabelText = QtWidgets.QLabel(self.centralwidget)
        self.yLabelText.setGeometry(QtCore.QRect(60, 60, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yLabelText.setFont(font)
        self.yLabelText.setObjectName("yLabelText")
        self.groupTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.groupTextLabel.setGeometry(QtCore.QRect(950, 90, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupTextLabel.setFont(font)
        self.groupTextLabel.setObjectName("groupTextLabel")
        self.plotTablePhase = plotTablePhase(self.centralwidget)
        self.plotTablePhase.setGeometry(QtCore.QRect(280, 430, 651, 401))
        self.plotTablePhase.setObjectName("plotTablePhase")
        self.plotTableGain = plotTableGain(self.centralwidget)
        self.plotTableGain.setGeometry(QtCore.QRect(280, 30, 651, 401))
        self.plotTableGain.setObjectName("plotTableGain")
        self.xLabelInput = QtWidgets.QLineEdit(self.centralwidget)
        self.xLabelInput.setGeometry(QtCore.QRect(40, 30, 171, 21))
        self.xLabelInput.setObjectName("xLabelInput")
        self.yLabelInput = QtWidgets.QLineEdit(self.centralwidget)
        self.yLabelInput.setGeometry(QtCore.QRect(40, 80, 171, 21))
        self.yLabelInput.setObjectName("yLabelInput")
        self.phaseUpdateLabel = QtWidgets.QPushButton(self.centralwidget)
        self.phaseUpdateLabel.setGeometry(QtCore.QRect(130, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.phaseUpdateLabel.setFont(font)
        self.phaseUpdateLabel.setObjectName("phaseUpdateLabel")
        self.gainUpdateLabel = QtWidgets.QPushButton(self.centralwidget)
        self.gainUpdateLabel.setGeometry(QtCore.QRect(60, 110, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gainUpdateLabel.setFont(font)
        self.gainUpdateLabel.setObjectName("gainUpdateLabel")
        self.removePlotsAction = QtWidgets.QPushButton(self.centralwidget)
        self.removePlotsAction.setGeometry(QtCore.QRect(980, 140, 151, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(197, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.removePlotsAction.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.removePlotsAction.setFont(font)
        self.removePlotsAction.setObjectName("removePlotsAction")
        self.transferFunction = QtWidgets.QStackedWidget(self.centralwidget)
        self.transferFunction.setGeometry(QtCore.QRect(40, 140, 181, 161))
        self.transferFunction.setObjectName("transferFunction")
        self.transferFunctionOption = QtWidgets.QWidget()
        self.transferFunctionOption.setObjectName("transferFunctionOption")
        self.transferFunctionAction = QtWidgets.QPushButton(self.transferFunctionOption)
        self.transferFunctionAction.setGeometry(QtCore.QRect(10, 30, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.transferFunctionAction.setFont(font)
        self.transferFunctionAction.setObjectName("transferFunctionAction")
        self.transferFunction.addWidget(self.transferFunctionOption)
        self.transferFunctionInput = QtWidgets.QWidget()
        self.transferFunctionInput.setObjectName("transferFunctionInput")
        self.transferFunctionMsg = QtWidgets.QLabel(self.transferFunctionInput)
        self.transferFunctionMsg.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.transferFunctionMsg.setObjectName("transferFunctionMsg")
        self.transferFunctionNumLabel = QtWidgets.QLabel(self.transferFunctionInput)
        self.transferFunctionNumLabel.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.transferFunctionNumLabel.setObjectName("transferFunctionNumLabel")
        self.transferFunctionDenLabel = QtWidgets.QLabel(self.transferFunctionInput)
        self.transferFunctionDenLabel.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.transferFunctionDenLabel.setObjectName("transferFunctionDenLabel")
        self.transferFunctionNumInput = QtWidgets.QLineEdit(self.transferFunctionInput)
        self.transferFunctionNumInput.setGeometry(QtCore.QRect(90, 40, 91, 20))
        self.transferFunctionNumInput.setObjectName("transferFunctionNumInput")
        self.transferFunctionDenInput = QtWidgets.QLineEdit(self.transferFunctionInput)
        self.transferFunctionDenInput.setGeometry(QtCore.QRect(90, 60, 91, 20))
        self.transferFunctionDenInput.setObjectName("transferFunctionDenInput")
        self.saveTransferFunction = QtWidgets.QPushButton(self.transferFunctionInput)
        self.saveTransferFunction.setGeometry(QtCore.QRect(20, 120, 75, 23))
        self.saveTransferFunction.setObjectName("saveTransferFunction")
        self.returnTransferFunction = QtWidgets.QPushButton(self.transferFunctionInput)
        self.returnTransferFunction.setGeometry(QtCore.QRect(100, 120, 75, 23))
        self.returnTransferFunction.setObjectName("returnTransferFunction")
        self.transferFunctionNameInput = QtWidgets.QLineEdit(self.transferFunctionInput)
        self.transferFunctionNameInput.setGeometry(QtCore.QRect(90, 80, 91, 20))
        self.transferFunctionNameInput.setObjectName("transferFunctionNameInput")
        self.transferFunctionNameLabel = QtWidgets.QLabel(self.transferFunctionInput)
        self.transferFunctionNameLabel.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.transferFunctionNameLabel.setObjectName("transferFunctionNameLabel")
        self.transferFunction.addWidget(self.transferFunctionInput)
        self.transferFunctionDisplay = QtWidgets.QWidget()
        self.transferFunctionDisplay.setObjectName("transferFunctionDisplay")
        self.transferFunctionNumDisplay = QtWidgets.QLabel(self.transferFunctionDisplay)
        self.transferFunctionNumDisplay.setGeometry(QtCore.QRect(40, 60, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.transferFunctionNumDisplay.setFont(font)
        self.transferFunctionNumDisplay.setText("")
        self.transferFunctionNumDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.transferFunctionNumDisplay.setObjectName("transferFunctionNumDisplay")
        self.transferFunctionDenDisplay = QtWidgets.QLabel(self.transferFunctionDisplay)
        self.transferFunctionDenDisplay.setGeometry(QtCore.QRect(40, 84, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.transferFunctionDenDisplay.setFont(font)
        self.transferFunctionDenDisplay.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.transferFunctionDenDisplay.setText("")
        self.transferFunctionDenDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.transferFunctionDenDisplay.setObjectName("transferFunctionDenDisplay")
        self.label_3 = QtWidgets.QLabel(self.transferFunctionDisplay)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.acceptTransferFunction = QtWidgets.QPushButton(self.transferFunctionDisplay)
        self.acceptTransferFunction.setGeometry(QtCore.QRect(20, 120, 75, 23))
        self.acceptTransferFunction.setObjectName("acceptTransferFunction")
        self.returnTransferFunctionInput = QtWidgets.QPushButton(self.transferFunctionDisplay)
        self.returnTransferFunctionInput.setGeometry(QtCore.QRect(100, 120, 75, 23))
        self.returnTransferFunctionInput.setObjectName("returnTransferFunctionInput")
        self.label_4 = QtWidgets.QLabel(self.transferFunctionDisplay)
        self.label_4.setGeometry(QtCore.QRect(40, 79, 141, 3))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.transferFunction.addWidget(self.transferFunctionDisplay)
        self.spiceFunction = QtWidgets.QStackedWidget(self.centralwidget)
        self.spiceFunction.setGeometry(QtCore.QRect(20, 320, 191, 101))
        self.spiceFunction.setObjectName("spiceFunction")
        self.spiceOption = QtWidgets.QWidget()
        self.spiceOption.setObjectName("spiceOption")
        self.spiceAction = QtWidgets.QPushButton(self.spiceOption)
        self.spiceAction.setGeometry(QtCore.QRect(30, 10, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spiceAction.setFont(font)
        self.spiceAction.setObjectName("spiceAction")
        self.spiceFunction.addWidget(self.spiceOption)
        self.spiceInput = QtWidgets.QWidget()
        self.spiceInput.setObjectName("spiceInput")
        self.spiceFunctionMsg = QtWidgets.QLabel(self.spiceInput)
        self.spiceFunctionMsg.setGeometry(QtCore.QRect(20, 0, 141, 16))
        self.spiceFunctionMsg.setObjectName("spiceFunctionMsg")
        self.saveSpiceFunction = QtWidgets.QPushButton(self.spiceInput)
        self.saveSpiceFunction.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.saveSpiceFunction.setObjectName("saveSpiceFunction")
        self.returnSpiceFunction = QtWidgets.QPushButton(self.spiceInput)
        self.returnSpiceFunction.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.returnSpiceFunction.setObjectName("returnSpiceFunction")
        self.LTSpiceNameInput = QtWidgets.QLineEdit(self.spiceInput)
        self.LTSpiceNameInput.setGeometry(QtCore.QRect(90, 20, 81, 21))
        self.LTSpiceNameInput.setObjectName("LTSpiceNameInput")
        self.label = QtWidgets.QLabel(self.spiceInput)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setObjectName("label")
        self.spiceFunction.addWidget(self.spiceInput)
        self.csvFunction = QtWidgets.QStackedWidget(self.centralwidget)
        self.csvFunction.setGeometry(QtCore.QRect(30, 470, 181, 121))
        self.csvFunction.setObjectName("csvFunction")
        self.csvOption = QtWidgets.QWidget()
        self.csvOption.setObjectName("csvOption")
        self.csvAction = QtWidgets.QPushButton(self.csvOption)
        self.csvAction.setGeometry(QtCore.QRect(20, 20, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.csvAction.setFont(font)
        self.csvAction.setObjectName("csvAction")
        self.csvFunction.addWidget(self.csvOption)
        self.csvInput = QtWidgets.QWidget()
        self.csvInput.setObjectName("csvInput")
        self.csvFunctionMsg = QtWidgets.QLabel(self.csvInput)
        self.csvFunctionMsg.setGeometry(QtCore.QRect(20, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.csvFunctionMsg.setFont(font)
        self.csvFunctionMsg.setObjectName("csvFunctionMsg")
        self.saveCsvFunction = QtWidgets.QPushButton(self.csvInput)
        self.saveCsvFunction.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.saveCsvFunction.setObjectName("saveCsvFunction")
        self.returnCsvFunction = QtWidgets.QPushButton(self.csvInput)
        self.returnCsvFunction.setGeometry(QtCore.QRect(100, 90, 75, 23))
        self.returnCsvFunction.setObjectName("returnCsvFunction")
        self.label_2 = QtWidgets.QLabel(self.csvInput)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.CSVNameInput = QtWidgets.QLineEdit(self.csvInput)
        self.CSVNameInput.setGeometry(QtCore.QRect(90, 50, 71, 20))
        self.CSVNameInput.setObjectName("CSVNameInput")
        self.csvFunction.addWidget(self.csvInput)
        self.transferFunctionCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.transferFunctionCheckBox.setGeometry(QtCore.QRect(90, 300, 70, 17))
        self.transferFunctionCheckBox.setChecked(True)
        self.transferFunctionCheckBox.setObjectName("transferFunctionCheckBox")
        self.spiceFunctionCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.spiceFunctionCheckBox.setGeometry(QtCore.QRect(90, 440, 70, 17))
        self.spiceFunctionCheckBox.setChecked(True)
        self.spiceFunctionCheckBox.setObjectName("spiceFunctionCheckBox")
        self.csvFunctionCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.csvFunctionCheckBox.setGeometry(QtCore.QRect(90, 610, 70, 17))
        self.csvFunctionCheckBox.setChecked(True)
        self.csvFunctionCheckBox.setObjectName("csvFunctionCheckBox")
        self.signalResponse = QtWidgets.QStackedWidget(self.centralwidget)
        self.signalResponse.setGeometry(QtCore.QRect(30, 630, 211, 211))
        self.signalResponse.setObjectName("signalResponse")
        self.signalFunctionOption = QtWidgets.QWidget()
        self.signalFunctionOption.setObjectName("signalFunctionOption")
        self.signalFunctionAction = QtWidgets.QPushButton(self.signalFunctionOption)
        self.signalFunctionAction.setGeometry(QtCore.QRect(20, 60, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.signalFunctionAction.setFont(font)
        self.signalFunctionAction.setObjectName("signalFunctionAction")
        self.signalResponse.addWidget(self.signalFunctionOption)
        self.signalFunctionMenu = QtWidgets.QWidget()
        self.signalFunctionMenu.setObjectName("signalFunctionMenu")
        self.layoutWidget = QtWidgets.QWidget(self.signalFunctionMenu)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 10, 111, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.impulseSignalAction = QtWidgets.QPushButton(self.layoutWidget)
        self.impulseSignalAction.setObjectName("impulseSignalAction")
        self.verticalLayout.addWidget(self.impulseSignalAction)
        self.stepSignalAction = QtWidgets.QPushButton(self.layoutWidget)
        self.stepSignalAction.setObjectName("stepSignalAction")
        self.verticalLayout.addWidget(self.stepSignalAction)
        self.sineSignalAction = QtWidgets.QPushButton(self.layoutWidget)
        self.sineSignalAction.setObjectName("sineSignalAction")
        self.verticalLayout.addWidget(self.sineSignalAction)
        self.squareSignalAction = QtWidgets.QPushButton(self.layoutWidget)
        self.squareSignalAction.setObjectName("squareSignalAction")
        self.verticalLayout.addWidget(self.squareSignalAction)
        self.triangleSignalAction = QtWidgets.QPushButton(self.layoutWidget)
        self.triangleSignalAction.setObjectName("triangleSignalAction")
        self.verticalLayout.addWidget(self.triangleSignalAction)
        self.returnSignalFunctionMenu = QtWidgets.QPushButton(self.layoutWidget)
        self.returnSignalFunctionMenu.setObjectName("returnSignalFunctionMenu")
        self.verticalLayout.addWidget(self.returnSignalFunctionMenu)
        self.signalResponse.addWidget(self.signalFunctionMenu)
        self.impulseSignalInput = QtWidgets.QWidget()
        self.impulseSignalInput.setObjectName("impulseSignalInput")
        self.returnImpulseSignal = QtWidgets.QPushButton(self.impulseSignalInput)
        self.returnImpulseSignal.setGeometry(QtCore.QRect(60, 138, 93, 28))
        self.returnImpulseSignal.setObjectName("returnImpulseSignal")
        self.impulseAmplitudeLabel = QtWidgets.QLabel(self.impulseSignalInput)
        self.impulseAmplitudeLabel.setGeometry(QtCore.QRect(50, 60, 50, 16))
        self.impulseAmplitudeLabel.setObjectName("impulseAmplitudeLabel")
        self.saveImpulseSignal = QtWidgets.QPushButton(self.impulseSignalInput)
        self.saveImpulseSignal.setGeometry(QtCore.QRect(60, 103, 93, 28))
        self.saveImpulseSignal.setObjectName("saveImpulseSignal")
        self.impulseAmplitudeInput = QtWidgets.QDoubleSpinBox(self.impulseSignalInput)
        self.impulseAmplitudeInput.setGeometry(QtCore.QRect(130, 50, 62, 24))
        self.impulseAmplitudeInput.setMaximum(100000.0)
        self.impulseAmplitudeInput.setObjectName("impulseAmplitudeInput")
        self.signalResponse.addWidget(self.impulseSignalInput)
        self.stepSignalInput = QtWidgets.QWidget()
        self.stepSignalInput.setObjectName("stepSignalInput")
        self.stepAmplitudeInput = QtWidgets.QDoubleSpinBox(self.stepSignalInput)
        self.stepAmplitudeInput.setGeometry(QtCore.QRect(110, 40, 62, 24))
        self.stepAmplitudeInput.setMaximum(100000.0)
        self.stepAmplitudeInput.setObjectName("stepAmplitudeInput")
        self.returnStepSignal = QtWidgets.QPushButton(self.stepSignalInput)
        self.returnStepSignal.setGeometry(QtCore.QRect(50, 130, 93, 28))
        self.returnStepSignal.setObjectName("returnStepSignal")
        self.stepLabel = QtWidgets.QLabel(self.stepSignalInput)
        self.stepLabel.setGeometry(QtCore.QRect(40, 50, 50, 16))
        self.stepLabel.setObjectName("stepLabel")
        self.saveStepSignal = QtWidgets.QPushButton(self.stepSignalInput)
        self.saveStepSignal.setGeometry(QtCore.QRect(50, 90, 93, 28))
        self.saveStepSignal.setObjectName("saveStepSignal")
        self.signalResponse.addWidget(self.stepSignalInput)
        self.sineSignalInput = QtWidgets.QWidget()
        self.sineSignalInput.setObjectName("sineSignalInput")
        self.sineAmplitudLabel = QtWidgets.QLabel(self.sineSignalInput)
        self.sineAmplitudLabel.setGeometry(QtCore.QRect(10, 10, 50, 16))
        self.sineAmplitudLabel.setObjectName("sineAmplitudLabel")
        self.sineAmplitudInput = QtWidgets.QDoubleSpinBox(self.sineSignalInput)
        self.sineAmplitudInput.setGeometry(QtCore.QRect(80, 10, 81, 24))
        self.sineAmplitudInput.setMaximum(10000.0)
        self.sineAmplitudInput.setObjectName("sineAmplitudInput")
        self.sineFrequencyLabel = QtWidgets.QLabel(self.sineSignalInput)
        self.sineFrequencyLabel.setGeometry(QtCore.QRect(10, 40, 90, 16))
        self.sineFrequencyLabel.setObjectName("sineFrequencyLabel")
        self.sineFrequencyInput = QtWidgets.QDoubleSpinBox(self.sineSignalInput)
        self.sineFrequencyInput.setGeometry(QtCore.QRect(110, 40, 71, 24))
        self.sineFrequencyInput.setMaximum(10000000.0)
        self.sineFrequencyInput.setObjectName("sineFrequencyInput")
        self.sinePhaneLabel = QtWidgets.QLabel(self.sineSignalInput)
        self.sinePhaneLabel.setGeometry(QtCore.QRect(20, 70, 47, 16))
        self.sinePhaneLabel.setObjectName("sinePhaneLabel")
        self.sinePhaseInput = QtWidgets.QDoubleSpinBox(self.sineSignalInput)
        self.sinePhaseInput.setGeometry(QtCore.QRect(90, 70, 91, 24))
        self.sinePhaseInput.setMinimum(-360.0)
        self.sinePhaseInput.setMaximum(360.0)
        self.sinePhaseInput.setObjectName("sinePhaseInput")
        self.saveSineSignal = QtWidgets.QPushButton(self.sineSignalInput)
        self.saveSineSignal.setGeometry(QtCore.QRect(50, 130, 93, 28))
        self.saveSineSignal.setObjectName("saveSineSignal")
        self.returnSineSignal = QtWidgets.QPushButton(self.sineSignalInput)
        self.returnSineSignal.setGeometry(QtCore.QRect(50, 160, 93, 28))
        self.returnSineSignal.setObjectName("returnSineSignal")
        self.sineDCLevelLabel = QtWidgets.QLabel(self.sineSignalInput)
        self.sineDCLevelLabel.setGeometry(QtCore.QRect(16, 100, 61, 20))
        self.sineDCLevelLabel.setObjectName("sineDCLevelLabel")
        self.sineDCLevelInput = QtWidgets.QDoubleSpinBox(self.sineSignalInput)
        self.sineDCLevelInput.setGeometry(QtCore.QRect(90, 100, 91, 24))
        self.sineDCLevelInput.setMinimum(-360.0)
        self.sineDCLevelInput.setMaximum(360.0)
        self.sineDCLevelInput.setObjectName("sineDCLevelInput")
        self.signalResponse.addWidget(self.sineSignalInput)
        self.squareSignalInput = QtWidgets.QWidget()
        self.squareSignalInput.setObjectName("squareSignalInput")
        self.squareAmplitudInput = QtWidgets.QDoubleSpinBox(self.squareSignalInput)
        self.squareAmplitudInput.setGeometry(QtCore.QRect(100, 10, 62, 24))
        self.squareAmplitudInput.setMaximum(100000.0)
        self.squareAmplitudInput.setObjectName("squareAmplitudInput")
        self.squareFrequencyInput = QtWidgets.QDoubleSpinBox(self.squareSignalInput)
        self.squareFrequencyInput.setGeometry(QtCore.QRect(120, 50, 62, 24))
        self.squareFrequencyInput.setMaximum(10000000.0)
        self.squareFrequencyInput.setObjectName("squareFrequencyInput")
        self.squareDutyInput = QtWidgets.QDoubleSpinBox(self.squareSignalInput)
        self.squareDutyInput.setGeometry(QtCore.QRect(110, 80, 62, 24))
        self.squareDutyInput.setMaximum(100.0)
        self.squareDutyInput.setObjectName("squareDutyInput")
        self.squareAmplitudLabel = QtWidgets.QLabel(self.squareSignalInput)
        self.squareAmplitudLabel.setGeometry(QtCore.QRect(20, 20, 50, 16))
        self.squareAmplitudLabel.setObjectName("squareAmplitudLabel")
        self.squareFrequencyLabel = QtWidgets.QLabel(self.squareSignalInput)
        self.squareFrequencyLabel.setGeometry(QtCore.QRect(20, 50, 90, 16))
        self.squareFrequencyLabel.setObjectName("squareFrequencyLabel")
        self.squareDutyLabel = QtWidgets.QLabel(self.squareSignalInput)
        self.squareDutyLabel.setGeometry(QtCore.QRect(20, 80, 51, 16))
        self.squareDutyLabel.setObjectName("squareDutyLabel")
        self.saveSquareSignal = QtWidgets.QPushButton(self.squareSignalInput)
        self.saveSquareSignal.setGeometry(QtCore.QRect(50, 135, 93, 28))
        self.saveSquareSignal.setObjectName("saveSquareSignal")
        self.returnSquareSignal = QtWidgets.QPushButton(self.squareSignalInput)
        self.returnSquareSignal.setGeometry(QtCore.QRect(50, 160, 93, 28))
        self.returnSquareSignal.setObjectName("returnSquareSignal")
        self.squareDCLevelInput = QtWidgets.QDoubleSpinBox(self.squareSignalInput)
        self.squareDCLevelInput.setGeometry(QtCore.QRect(110, 110, 62, 24))
        self.squareDCLevelInput.setMaximum(100.0)
        self.squareDCLevelInput.setObjectName("squareDCLevelInput")
        self.squareDCLevelLabel = QtWidgets.QLabel(self.squareSignalInput)
        self.squareDCLevelLabel.setGeometry(QtCore.QRect(10, 110, 61, 20))
        self.squareDCLevelLabel.setObjectName("squareDCLevelLabel")
        self.signalResponse.addWidget(self.squareSignalInput)
        self.triangleSignalInput = QtWidgets.QWidget()
        self.triangleSignalInput.setObjectName("triangleSignalInput")
        self.triangleAmplitudLabel = QtWidgets.QLabel(self.triangleSignalInput)
        self.triangleAmplitudLabel.setGeometry(QtCore.QRect(20, 20, 50, 16))
        self.triangleAmplitudLabel.setObjectName("triangleAmplitudLabel")
        self.triangleAmplitudInput = QtWidgets.QDoubleSpinBox(self.triangleSignalInput)
        self.triangleAmplitudInput.setGeometry(QtCore.QRect(100, 10, 62, 24))
        self.triangleAmplitudInput.setMaximum(100000.0)
        self.triangleAmplitudInput.setObjectName("triangleAmplitudInput")
        self.triangleFrequencyLabel = QtWidgets.QLabel(self.triangleSignalInput)
        self.triangleFrequencyLabel.setGeometry(QtCore.QRect(10, 50, 90, 16))
        self.triangleFrequencyLabel.setObjectName("triangleFrequencyLabel")
        self.triangleFrequencyInput = QtWidgets.QDoubleSpinBox(self.triangleSignalInput)
        self.triangleFrequencyInput.setGeometry(QtCore.QRect(110, 40, 62, 24))
        self.triangleFrequencyInput.setMaximum(10000000.0)
        self.triangleFrequencyInput.setObjectName("triangleFrequencyInput")
        self.triangleSymetryLabel = QtWidgets.QLabel(self.triangleSignalInput)
        self.triangleSymetryLabel.setGeometry(QtCore.QRect(20, 80, 73, 16))
        self.triangleSymetryLabel.setObjectName("triangleSymetryLabel")
        self.triangleSymetryInput = QtWidgets.QDoubleSpinBox(self.triangleSignalInput)
        self.triangleSymetryInput.setGeometry(QtCore.QRect(110, 80, 62, 24))
        self.triangleSymetryInput.setMaximum(100.0)
        self.triangleSymetryInput.setObjectName("triangleSymetryInput")
        self.saveTriangleSignal = QtWidgets.QPushButton(self.triangleSignalInput)
        self.saveTriangleSignal.setGeometry(QtCore.QRect(60, 140, 93, 28))
        self.saveTriangleSignal.setObjectName("saveTriangleSignal")
        self.returnTriangleSignal = QtWidgets.QPushButton(self.triangleSignalInput)
        self.returnTriangleSignal.setGeometry(QtCore.QRect(60, 169, 93, 28))
        self.returnTriangleSignal.setObjectName("returnTriangleSignal")
        self.triangleDCLevelInput = QtWidgets.QDoubleSpinBox(self.triangleSignalInput)
        self.triangleDCLevelInput.setGeometry(QtCore.QRect(110, 110, 62, 24))
        self.triangleDCLevelInput.setMaximum(100.0)
        self.triangleDCLevelInput.setObjectName("triangleDCLevelInput")
        self.triangleDCLevelLabel = QtWidgets.QLabel(self.triangleSignalInput)
        self.triangleDCLevelLabel.setGeometry(QtCore.QRect(20, 110, 73, 16))
        self.triangleDCLevelLabel.setObjectName("triangleDCLevelLabel")
        self.signalResponse.addWidget(self.triangleSignalInput)
        self.arbitrarySignalInput = QtWidgets.QWidget()
        self.arbitrarySignalInput.setObjectName("arbitrarySignalInput")
        self.signalResponse.addWidget(self.arbitrarySignalInput)
        self.signalResponseCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.signalResponseCheckBox.setGeometry(QtCore.QRect(90, 840, 70, 17))
        self.signalResponseCheckBox.setChecked(True)
        self.signalResponseCheckBox.setObjectName("signalResponseCheckBox")
        self.itbaLogo = QtWidgets.QLabel(self.centralwidget)
        self.itbaLogo.setGeometry(QtCore.QRect(940, 20, 221, 71))
        self.itbaLogo.setText("")
        self.itbaLogo.setPixmap(QtGui.QPixmap(":/prefijoNuevo/itbaLogo.png"))
        self.itbaLogo.setObjectName("itbaLogo")
        self.Same_plot_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Same_plot_checkbox.setGeometry(QtCore.QRect(540, 840, 151, 17))
        self.Same_plot_checkbox.setObjectName("Same_plot_checkbox")
        bodePlotterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(bodePlotterWindow)
        self.statusbar.setObjectName("statusbar")
        bodePlotterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(bodePlotterWindow)
        self.transferFunction.setCurrentIndex(0)
        self.spiceFunction.setCurrentIndex(0)
        self.csvFunction.setCurrentIndex(0)
        self.signalResponse.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bodePlotterWindow)

    def retranslateUi(self, bodePlotterWindow):
        _translate = QtCore.QCoreApplication.translate
        bodePlotterWindow.setWindowTitle(_translate("bodePlotterWindow", "MainWindow"))
        self.xLabelText.setText(_translate("bodePlotterWindow", "Etiqueta EJE X"))
        self.yLabelText.setText(_translate("bodePlotterWindow", "Etiqueta EJE Y"))
        self.groupTextLabel.setText(_translate("bodePlotterWindow", "Plot Tool - Grupo 6"))
        self.phaseUpdateLabel.setText(_translate("bodePlotterWindow", "Φ"))
        self.gainUpdateLabel.setText(_translate("bodePlotterWindow", "| H(S)|"))
        self.removePlotsAction.setText(_translate("bodePlotterWindow", "Borrar Todo"))
        self.transferFunctionAction.setText(_translate("bodePlotterWindow", "H(S)"))
        self.transferFunctionMsg.setText(_translate("bodePlotterWindow", "Ingrese la Funcion de Transferencia"))
        self.transferFunctionNumLabel.setText(_translate("bodePlotterWindow", "Numerador"))
        self.transferFunctionDenLabel.setText(_translate("bodePlotterWindow", "Denominador"))
        self.saveTransferFunction.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.returnTransferFunction.setText(_translate("bodePlotterWindow", "Volver"))
        self.transferFunctionNameLabel.setText(_translate("bodePlotterWindow", "Nombre"))
        self.label_3.setText(_translate("bodePlotterWindow", "H(S)="))
        self.acceptTransferFunction.setText(_translate("bodePlotterWindow", "Aceptar"))
        self.returnTransferFunctionInput.setText(_translate("bodePlotterWindow", "Volver"))
        self.label_4.setText(_translate("bodePlotterWindow", "_______________________"))
        self.spiceAction.setText(_translate("bodePlotterWindow", "SPICE"))
        self.spiceFunctionMsg.setText(_translate("bodePlotterWindow", "Busque el archivo de LTSpice"))
        self.saveSpiceFunction.setText(_translate("bodePlotterWindow", "Buscar"))
        self.returnSpiceFunction.setText(_translate("bodePlotterWindow", "Volver"))
        self.label.setText(_translate("bodePlotterWindow", "Nombre"))
        self.csvAction.setText(_translate("bodePlotterWindow", "Medición"))
        self.csvFunctionMsg.setText(_translate("bodePlotterWindow", "Busque el archivo con las mediciones"))
        self.saveCsvFunction.setText(_translate("bodePlotterWindow", "Buscar"))
        self.returnCsvFunction.setText(_translate("bodePlotterWindow", "Volver"))
        self.label_2.setText(_translate("bodePlotterWindow", "Nombre"))
        self.transferFunctionCheckBox.setText(_translate("bodePlotterWindow", "Incluir "))
        self.spiceFunctionCheckBox.setText(_translate("bodePlotterWindow", "Incluir "))
        self.csvFunctionCheckBox.setText(_translate("bodePlotterWindow", "Incluir "))
        self.signalFunctionAction.setText(_translate("bodePlotterWindow", "Señales"))
        self.impulseSignalAction.setText(_translate("bodePlotterWindow", "Impulso"))
        self.stepSignalAction.setText(_translate("bodePlotterWindow", "Escalón"))
        self.sineSignalAction.setText(_translate("bodePlotterWindow", "Senoidal"))
        self.squareSignalAction.setText(_translate("bodePlotterWindow", "Cuadrada"))
        self.triangleSignalAction.setText(_translate("bodePlotterWindow", "Triangular"))
        self.returnSignalFunctionMenu.setText(_translate("bodePlotterWindow", "Volver"))
        self.returnImpulseSignal.setText(_translate("bodePlotterWindow", "Volver"))
        self.impulseAmplitudeLabel.setText(_translate("bodePlotterWindow", "Amplitud"))
        self.saveImpulseSignal.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.returnStepSignal.setText(_translate("bodePlotterWindow", "Volver"))
        self.stepLabel.setText(_translate("bodePlotterWindow", "Amplitud"))
        self.saveStepSignal.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.sineAmplitudLabel.setText(_translate("bodePlotterWindow", "Amplitud"))
        self.sineFrequencyLabel.setText(_translate("bodePlotterWindow", "Frecuencia (Hz)"))
        self.sinePhaneLabel.setText(_translate("bodePlotterWindow", "Fase (°)"))
        self.saveSineSignal.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.returnSineSignal.setText(_translate("bodePlotterWindow", "Volver"))
        self.sineDCLevelLabel.setText(_translate("bodePlotterWindow", "DC Level"))
        self.squareAmplitudLabel.setText(_translate("bodePlotterWindow", "Amplitud"))
        self.squareFrequencyLabel.setText(_translate("bodePlotterWindow", "Frecuencia (Hz)"))
        self.squareDutyLabel.setText(_translate("bodePlotterWindow", "Duty (%)"))
        self.saveSquareSignal.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.returnSquareSignal.setText(_translate("bodePlotterWindow", "Volver"))
        self.squareDCLevelLabel.setText(_translate("bodePlotterWindow", "DC level"))
        self.triangleAmplitudLabel.setText(_translate("bodePlotterWindow", "Amplitud"))
        self.triangleFrequencyLabel.setText(_translate("bodePlotterWindow", "Frecuencia (Hz)"))
        self.triangleSymetryLabel.setText(_translate("bodePlotterWindow", "Symetry (%)"))
        self.saveTriangleSignal.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.returnTriangleSignal.setText(_translate("bodePlotterWindow", "Volver"))
        self.triangleDCLevelLabel.setText(_translate("bodePlotterWindow", "DC level"))
        self.signalResponseCheckBox.setText(_translate("bodePlotterWindow", "Incluir "))
        self.Same_plot_checkbox.setText(_translate("bodePlotterWindow", "Plotear en el mismo gráfico"))
from src.ui.plottablegain import plotTableGain
from src.ui.plottablephase import plotTablePhase
from src.resources import itbaLogo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bodePlotterWindow = QtWidgets.QMainWindow()
    ui = Ui_bodePlotterWindow()
    ui.setupUi(bodePlotterWindow)
    bodePlotterWindow.show()
    sys.exit(app.exec_())
