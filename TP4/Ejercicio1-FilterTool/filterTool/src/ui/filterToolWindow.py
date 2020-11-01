# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\filterToolWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filterToolWindow(object):
    def setupUi(self, filterToolWindow):
        filterToolWindow.setObjectName("filterToolWindow")
        filterToolWindow.resize(933, 767)
        self.centralwidget = QtWidgets.QWidget(filterToolWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stages = QtWidgets.QStackedWidget(self.centralwidget)
        self.stages.setGeometry(QtCore.QRect(10, 10, 901, 711))
        self.stages.setObjectName("stages")
        self.stageOne = QtWidgets.QWidget()
        self.stageOne.setObjectName("stageOne")
        self.filterTypeOption = QtWidgets.QComboBox(self.stageOne)
        self.filterTypeOption.setGeometry(QtCore.QRect(20, 70, 221, 21))
        self.filterTypeOption.setObjectName("filterTypeOption")
        self.filterTypeOption.addItem("")
        self.filterTypeOption.addItem("")
        self.filterTypeOption.addItem("")
        self.filterTypeOption.addItem("")
        self.filterTypeOption.addItem("")
        self.approxTypeOption = QtWidgets.QComboBox(self.stageOne)
        self.approxTypeOption.setGeometry(QtCore.QRect(20, 130, 221, 21))
        self.approxTypeOption.setObjectName("approxTypeOption")
        self.approxTypeOption.addItem("")
        self.approxTypeOption.addItem("")
        self.approxTypeOption.addItem("")
        self.filterTypeOptionLabel = QtWidgets.QLabel(self.stageOne)
        self.filterTypeOptionLabel.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.filterTypeOptionLabel.setObjectName("filterTypeOptionLabel")
        self.aproxTypeOptionLabel = QtWidgets.QLabel(self.stageOne)
        self.aproxTypeOptionLabel.setGeometry(QtCore.QRect(30, 110, 71, 16))
        self.aproxTypeOptionLabel.setObjectName("aproxTypeOptionLabel")
        self.filterTypeOptionLabel_2 = QtWidgets.QLabel(self.stageOne)
        self.filterTypeOptionLabel_2.setGeometry(QtCore.QRect(20, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filterTypeOptionLabel_2.setFont(font)
        self.filterTypeOptionLabel_2.setObjectName("filterTypeOptionLabel_2")
        self.filterParameters = QtWidgets.QStackedWidget(self.stageOne)
        self.filterParameters.setGeometry(QtCore.QRect(20, 170, 301, 251))
        self.filterParameters.setObjectName("filterParameters")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.filterParameters.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.aaLabel = QtWidgets.QLabel(self.page_4)
        self.aaLabel.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.aaLabel.setObjectName("aaLabel")
        self.aaInput = QtWidgets.QLineEdit(self.page_4)
        self.aaInput.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.aaInput.setObjectName("aaInput")
        self.apLabel = QtWidgets.QLabel(self.page_4)
        self.apLabel.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.apLabel.setObjectName("apLabel")
        self.apInput = QtWidgets.QLineEdit(self.page_4)
        self.apInput.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.apInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.apInput.setObjectName("apInput")
        self.faLabel = QtWidgets.QLabel(self.page_4)
        self.faLabel.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.faLabel.setObjectName("faLabel")
        self.faInput = QtWidgets.QLineEdit(self.page_4)
        self.faInput.setGeometry(QtCore.QRect(20, 150, 113, 20))
        self.faInput.setObjectName("faInput")
        self.fpInput = QtWidgets.QLabel(self.page_4)
        self.fpInput.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.fpInput.setObjectName("fpInput")
        self.fpInput_2 = QtWidgets.QLineEdit(self.page_4)
        self.fpInput_2.setGeometry(QtCore.QRect(20, 200, 113, 20))
        self.fpInput_2.setObjectName("fpInput_2")
        self.filterParameters.addWidget(self.page_4)
        self.filterOrderLabel = QtWidgets.QLabel(self.stageOne)
        self.filterOrderLabel.setGeometry(QtCore.QRect(40, 440, 71, 16))
        self.filterOrderLabel.setObjectName("filterOrderLabel")
        self.filterOrderInput = QtWidgets.QLineEdit(self.stageOne)
        self.filterOrderInput.setGeometry(QtCore.QRect(40, 460, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.filterOrderInput.setFont(font)
        self.filterOrderInput.setObjectName("filterOrderInput")
        self.qmaxLabel = QtWidgets.QLabel(self.stageOne)
        self.qmaxLabel.setGeometry(QtCore.QRect(40, 500, 71, 16))
        self.qmaxLabel.setObjectName("qmaxLabel")
        self.qmaxInput = QtWidgets.QLineEdit(self.stageOne)
        self.qmaxInput.setGeometry(QtCore.QRect(40, 520, 113, 20))
        self.qmaxInput.setObjectName("qmaxInput")
        self.denormLabel = QtWidgets.QLabel(self.stageOne)
        self.denormLabel.setGeometry(QtCore.QRect(40, 560, 81, 16))
        self.denormLabel.setObjectName("denormLabel")
        self.denormInput = QtWidgets.QLineEdit(self.stageOne)
        self.denormInput.setGeometry(QtCore.QRect(40, 580, 113, 20))
        self.denormInput.setObjectName("denormInput")
        self.filterToolPlotTable = filterToolPlot(self.stageOne)
        self.filterToolPlotTable.setGeometry(QtCore.QRect(330, 30, 551, 381))
        self.filterToolPlotTable.setObjectName("filterToolPlotTable")
        self.goStageTwoButton = QtWidgets.QPushButton(self.stageOne)
        self.goStageTwoButton.setGeometry(QtCore.QRect(60, 670, 91, 23))
        self.goStageTwoButton.setObjectName("goStageTwoButton")
        self.label = QtWidgets.QLabel(self.stageOne)
        self.label.setGeometry(QtCore.QRect(410, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plotTypeOptionInput = QtWidgets.QComboBox(self.stageOne)
        self.plotTypeOptionInput.setGeometry(QtCore.QRect(490, 440, 221, 21))
        self.plotTypeOptionInput.setObjectName("plotTypeOptionInput")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionLabel = QtWidgets.QLabel(self.stageOne)
        self.plotTypeOptionLabel.setGeometry(QtCore.QRect(460, 440, 31, 16))
        self.plotTypeOptionLabel.setObjectName("plotTypeOptionLabel")
        self.acceptParametersStageOne = QtWidgets.QPushButton(self.stageOne)
        self.acceptParametersStageOne.setGeometry(QtCore.QRect(50, 620, 111, 23))
        self.acceptParametersStageOne.setObjectName("acceptParametersStageOne")
        self.stages.addWidget(self.stageOne)
        self.stageTwo = QtWidgets.QWidget()
        self.stageTwo.setObjectName("stageTwo")
        self.label_2 = QtWidgets.QLabel(self.stageTwo)
        self.label_2.setGeometry(QtCore.QRect(410, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.returnStageOneButton = QtWidgets.QPushButton(self.stageTwo)
        self.returnStageOneButton.setGeometry(QtCore.QRect(60, 670, 101, 23))
        self.returnStageOneButton.setObjectName("returnStageOneButton")
        self.parametersInfo = QtWidgets.QWidget(self.stageTwo)
        self.parametersInfo.setGeometry(QtCore.QRect(450, 470, 351, 201))
        self.parametersInfo.setObjectName("parametersInfo")
        self.widget_2 = filterToolPlotStage2(self.stageTwo)
        self.widget_2.setGeometry(QtCore.QRect(330, 30, 550, 381))
        self.widget_2.setObjectName("widget_2")
        self.parametersInfoLabel = QtWidgets.QLabel(self.stageTwo)
        self.parametersInfoLabel.setGeometry(QtCore.QRect(510, 440, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.parametersInfoLabel.setFont(font)
        self.parametersInfoLabel.setObjectName("parametersInfoLabel")
        self.parametersInfoLabel_2 = QtWidgets.QLabel(self.stageTwo)
        self.parametersInfoLabel_2.setGeometry(QtCore.QRect(40, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.parametersInfoLabel_2.setFont(font)
        self.parametersInfoLabel_2.setObjectName("parametersInfoLabel_2")
        self.widget_3 = QtWidgets.QWidget(self.stageTwo)
        self.widget_3.setGeometry(QtCore.QRect(10, 80, 301, 301))
        self.widget_3.setObjectName("widget_3")
        self.zeroTransferFunctionOrder = QtWidgets.QComboBox(self.stageTwo)
        self.zeroTransferFunctionOrder.setGeometry(QtCore.QRect(90, 390, 141, 22))
        self.zeroTransferFunctionOrder.setObjectName("zeroTransferFunctionOrder")
        self.zeroTransferFunctionOrder.addItem("")
        self.zeroTransferFunctionOrder.addItem("")
        self.poleTransferFunctionOrder = QtWidgets.QComboBox(self.stageTwo)
        self.poleTransferFunctionOrder.setGeometry(QtCore.QRect(90, 430, 141, 22))
        self.poleTransferFunctionOrder.setObjectName("poleTransferFunctionOrder")
        self.poleTransferFunctionOrder.addItem("")
        self.poleTransferFunctionOrder.addItem("")
        self.zeroLabel = QtWidgets.QLabel(self.stageTwo)
        self.zeroLabel.setGeometry(QtCore.QRect(50, 390, 41, 16))
        self.zeroLabel.setObjectName("zeroLabel")
        self.poleLabel = QtWidgets.QLabel(self.stageTwo)
        self.poleLabel.setGeometry(QtCore.QRect(50, 430, 31, 16))
        self.poleLabel.setObjectName("poleLabel")
        self.stages.addWidget(self.stageTwo)
        filterToolWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(filterToolWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        filterToolWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(filterToolWindow)
        self.statusbar.setObjectName("statusbar")
        filterToolWindow.setStatusBar(self.statusbar)

        self.retranslateUi(filterToolWindow)
        self.stages.setCurrentIndex(0)
        self.filterParameters.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(filterToolWindow)

    def retranslateUi(self, filterToolWindow):
        _translate = QtCore.QCoreApplication.translate
        filterToolWindow.setWindowTitle(_translate("filterToolWindow", "MainWindow"))
        self.filterTypeOption.setItemText(0, _translate("filterToolWindow", "Low-Pass"))
        self.filterTypeOption.setItemText(1, _translate("filterToolWindow", "High-Pass"))
        self.filterTypeOption.setItemText(2, _translate("filterToolWindow", "Band-Pass"))
        self.filterTypeOption.setItemText(3, _translate("filterToolWindow", "Band-Rejection"))
        self.filterTypeOption.setItemText(4, _translate("filterToolWindow", "Group Delay"))
        self.approxTypeOption.setItemText(0, _translate("filterToolWindow", "Cauer"))
        self.approxTypeOption.setItemText(1, _translate("filterToolWindow", "Gauss"))
        self.approxTypeOption.setItemText(2, _translate("filterToolWindow", "Legendre"))
        self.filterTypeOptionLabel.setText(_translate("filterToolWindow", "Filter Type"))
        self.aproxTypeOptionLabel.setText(_translate("filterToolWindow", "Approximation"))
        self.filterTypeOptionLabel_2.setText(_translate("filterToolWindow", "Filter Parameters"))
        self.aaLabel.setText(_translate("filterToolWindow", "Aa [DB] "))
        self.apLabel.setText(_translate("filterToolWindow", "Ap [DB] "))
        self.faLabel.setText(_translate("filterToolWindow", "fa [Hz] "))
        self.fpInput.setText(_translate("filterToolWindow", "fp [Hz] "))
        self.filterOrderLabel.setText(_translate("filterToolWindow", "Filter Order"))
        self.qmaxLabel.setText(_translate("filterToolWindow", "Maximum Q"))
        self.denormLabel.setText(_translate("filterToolWindow", "Denormalization"))
        self.goStageTwoButton.setText(_translate("filterToolWindow", "Go To Stage 2"))
        self.label.setText(_translate("filterToolWindow", "Stage 1"))
        self.plotTypeOptionInput.setItemText(0, _translate("filterToolWindow", "Magnitude"))
        self.plotTypeOptionInput.setItemText(1, _translate("filterToolWindow", "Phase"))
        self.plotTypeOptionInput.setItemText(2, _translate("filterToolWindow", "Attenuation"))
        self.plotTypeOptionInput.setItemText(3, _translate("filterToolWindow", "Attenuation - Normalized"))
        self.plotTypeOptionInput.setItemText(4, _translate("filterToolWindow", "Group Delay"))
        self.plotTypeOptionInput.setItemText(5, _translate("filterToolWindow", "Poles and Zeros"))
        self.plotTypeOptionInput.setItemText(6, _translate("filterToolWindow", "Impulse Response"))
        self.plotTypeOptionInput.setItemText(7, _translate("filterToolWindow", "Step Response"))
        self.plotTypeOptionInput.setItemText(8, _translate("filterToolWindow", "Maximum Q"))
        self.plotTypeOptionLabel.setText(_translate("filterToolWindow", "Plot"))
        self.acceptParametersStageOne.setText(_translate("filterToolWindow", "Enter Parameters"))
        self.label_2.setText(_translate("filterToolWindow", "Stage 2"))
        self.returnStageOneButton.setText(_translate("filterToolWindow", "Return to Stage 1"))
        self.parametersInfoLabel.setText(_translate("filterToolWindow", "Filter Parameters"))
        self.parametersInfoLabel_2.setText(_translate("filterToolWindow", "Transfer Functions"))
        self.zeroTransferFunctionOrder.setItemText(0, _translate("filterToolWindow", "First Order"))
        self.zeroTransferFunctionOrder.setItemText(1, _translate("filterToolWindow", "Second Order"))
        self.poleTransferFunctionOrder.setItemText(0, _translate("filterToolWindow", "First Order"))
        self.poleTransferFunctionOrder.setItemText(1, _translate("filterToolWindow", "Second Order"))
        self.zeroLabel.setText(_translate("filterToolWindow", "Zeros"))
        self.poleLabel.setText(_translate("filterToolWindow", "Poles"))
from filtertoolplot import filterToolPlot
from filtertoolplotstage2 import filterToolPlotStage2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filterToolWindow = QtWidgets.QMainWindow()
    ui = Ui_filterToolWindow()
    ui.setupUi(filterToolWindow)
    filterToolWindow.show()
    sys.exit(app.exec_())
