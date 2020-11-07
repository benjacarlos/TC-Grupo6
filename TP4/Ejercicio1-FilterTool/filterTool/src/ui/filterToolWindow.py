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
        self.groupDelayParameters = QtWidgets.QWidget()
        self.groupDelayParameters.setObjectName("groupDelayParameters")
        self.wrgInput = QtWidgets.QLineEdit(self.groupDelayParameters)
        self.wrgInput.setGeometry(QtCore.QRect(30, 50, 113, 20))
        self.wrgInput.setObjectName("wrgInput")
        self.tolInput = QtWidgets.QLineEdit(self.groupDelayParameters)
        self.tolInput.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.tolInput.setObjectName("tolInput")
        self.tauInput = QtWidgets.QLineEdit(self.groupDelayParameters)
        self.tauInput.setGeometry(QtCore.QRect(30, 130, 113, 20))
        self.tauInput.setObjectName("tauInput")
        self.wrgLabel = QtWidgets.QLabel(self.groupDelayParameters)
        self.wrgLabel.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.wrgLabel.setObjectName("wrgLabel")
        self.tolLabel = QtWidgets.QLabel(self.groupDelayParameters)
        self.tolLabel.setGeometry(QtCore.QRect(30, 70, 71, 16))
        self.tolLabel.setObjectName("tolLabel")
        self.tauLabel = QtWidgets.QLabel(self.groupDelayParameters)
        self.tauLabel.setGeometry(QtCore.QRect(30, 110, 71, 16))
        self.tauLabel.setObjectName("tauLabel")
        self.filterParameters.addWidget(self.groupDelayParameters)
        self.freqParameters = QtWidgets.QWidget()
        self.freqParameters.setObjectName("freqParameters")
        self.aaLabel = QtWidgets.QLabel(self.freqParameters)
        self.aaLabel.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.aaLabel.setObjectName("aaLabel")
        self.aaInput = QtWidgets.QLineEdit(self.freqParameters)
        self.aaInput.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.aaInput.setObjectName("aaInput")
        self.apLabel = QtWidgets.QLabel(self.freqParameters)
        self.apLabel.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.apLabel.setObjectName("apLabel")
        self.apInput = QtWidgets.QLineEdit(self.freqParameters)
        self.apInput.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.apInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.apInput.setObjectName("apInput")
        self.faLabel = QtWidgets.QLabel(self.freqParameters)
        self.faLabel.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.faLabel.setObjectName("faLabel")
        self.faInput = QtWidgets.QLineEdit(self.freqParameters)
        self.faInput.setGeometry(QtCore.QRect(20, 150, 113, 20))
        self.faInput.setObjectName("faInput")
        self.fpLabel = QtWidgets.QLabel(self.freqParameters)
        self.fpLabel.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.fpLabel.setObjectName("fpLabel")
        self.fpInput = QtWidgets.QLineEdit(self.freqParameters)
        self.fpInput.setGeometry(QtCore.QRect(20, 200, 113, 20))
        self.fpInput.setObjectName("fpInput")
        self.hiddenWidget = QtWidgets.QStackedWidget(self.freqParameters)
        self.hiddenWidget.setGeometry(QtCore.QRect(160, 30, 141, 91))
        self.hiddenWidget.setObjectName("hiddenWidget")
        self.dontShowHidden = QtWidgets.QWidget()
        self.dontShowHidden.setObjectName("dontShowHidden")
        self.hiddenWidget.addWidget(self.dontShowHidden)
        self.showHiddenWidget = QtWidgets.QWidget()
        self.showHiddenWidget.setObjectName("showHiddenWidget")
        self.famLabel = QtWidgets.QLabel(self.showHiddenWidget)
        self.famLabel.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.famLabel.setObjectName("famLabel")
        self.famInput = QtWidgets.QLineEdit(self.showHiddenWidget)
        self.famInput.setGeometry(QtCore.QRect(0, 20, 113, 20))
        self.famInput.setObjectName("famInput")
        self.fpmLabel = QtWidgets.QLabel(self.showHiddenWidget)
        self.fpmLabel.setGeometry(QtCore.QRect(0, 50, 71, 16))
        self.fpmLabel.setObjectName("fpmLabel")
        self.fpmInput = QtWidgets.QLineEdit(self.showHiddenWidget)
        self.fpmInput.setGeometry(QtCore.QRect(0, 70, 113, 20))
        self.fpmInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fpmInput.setObjectName("fpmInput")
        self.hiddenWidget.addWidget(self.showHiddenWidget)
        self.filterParameters.addWidget(self.freqParameters)
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
        self.goStageTwoButton.setGeometry(QtCore.QRect(810, 680, 91, 23))
        self.goStageTwoButton.setObjectName("goStageTwoButton")
        self.label = QtWidgets.QLabel(self.stageOne)
        self.label.setGeometry(QtCore.QRect(410, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plotTypeOptionInput = QtWidgets.QComboBox(self.stageOne)
        self.plotTypeOptionInput.setGeometry(QtCore.QRect(490, 440, 301, 21))
        self.plotTypeOptionInput.setObjectName("plotTypeOptionInput")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionInput.addItem("")
        self.plotTypeOptionLabel = QtWidgets.QLabel(self.stageOne)
        self.plotTypeOptionLabel.setGeometry(QtCore.QRect(450, 440, 31, 16))
        self.plotTypeOptionLabel.setObjectName("plotTypeOptionLabel")
        self.acceptParametersStageOne = QtWidgets.QPushButton(self.stageOne)
        self.acceptParametersStageOne.setGeometry(QtCore.QRect(50, 620, 111, 23))
        self.acceptParametersStageOne.setObjectName("acceptParametersStageOne")
        self.filterDesignedLabel = QtWidgets.QLabel(self.stageOne)
        self.filterDesignedLabel.setGeometry(QtCore.QRect(450, 480, 31, 16))
        self.filterDesignedLabel.setObjectName("filterDesignedLabel")
        self.filterDesignedLabelCombo = QtWidgets.QComboBox(self.stageOne)
        self.filterDesignedLabelCombo.setGeometry(QtCore.QRect(490, 480, 301, 21))
        self.filterDesignedLabelCombo.setObjectName("filterDesignedLabelCombo")
        self.plotAllCheckBox = QtWidgets.QCheckBox(self.stageOne)
        self.plotAllCheckBox.setGeometry(QtCore.QRect(600, 520, 70, 17))
        self.plotAllCheckBox.setChecked(True)
        self.plotAllCheckBox.setObjectName("plotAllCheckBox")
        self.hsLabel = QtWidgets.QLabel(self.stageOne)
        self.hsLabel.setGeometry(QtCore.QRect(360, 610, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hsLabel.setFont(font)
        self.hsLabel.setObjectName("hsLabel")
        self.hsLabelNum = QtWidgets.QLabel(self.stageOne)
        self.hsLabelNum.setGeometry(QtCore.QRect(420, 610, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hsLabelNum.setFont(font)
        self.hsLabelNum.setText("")
        self.hsLabelNum.setAlignment(QtCore.Qt.AlignCenter)
        self.hsLabelNum.setObjectName("hsLabelNum")
        self.hsLabelDen = QtWidgets.QLabel(self.stageOne)
        self.hsLabelDen.setGeometry(QtCore.QRect(420, 630, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hsLabelDen.setFont(font)
        self.hsLabelDen.setText("")
        self.hsLabelDen.setAlignment(QtCore.Qt.AlignCenter)
        self.hsLabelDen.setObjectName("hsLabelDen")
        self.hsLabelNum_3 = QtWidgets.QLabel(self.stageOne)
        self.hsLabelNum_3.setGeometry(QtCore.QRect(420, 620, 461, 16))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.hsLabelNum_3.setFont(font)
        self.hsLabelNum_3.setObjectName("hsLabelNum_3")
        self.hiddenWarning = QtWidgets.QStackedWidget(self.stageOne)
        self.hiddenWarning.setGeometry(QtCore.QRect(190, 500, 171, 141))
        self.hiddenWarning.setObjectName("hiddenWarning")
        self.warningIsHidden = QtWidgets.QWidget()
        self.warningIsHidden.setObjectName("warningIsHidden")
        self.hiddenWarning.addWidget(self.warningIsHidden)
        self.warningNotHidden = QtWidgets.QWidget()
        self.warningNotHidden.setObjectName("warningNotHidden")
        self.okToRemove = QtWidgets.QPushButton(self.warningNotHidden)
        self.okToRemove.setGeometry(QtCore.QRect(20, 100, 61, 23))
        self.okToRemove.setObjectName("okToRemove")
        self.noOkToRemove = QtWidgets.QPushButton(self.warningNotHidden)
        self.noOkToRemove.setGeometry(QtCore.QRect(90, 100, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.noOkToRemove.setFont(font)
        self.noOkToRemove.setObjectName("noOkToRemove")
        self.label_3 = QtWidgets.QLabel(self.warningNotHidden)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 151, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.warningNotHidden)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.warningNotHidden)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.warningNotHidden)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 131, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.hiddenWarning.addWidget(self.warningNotHidden)
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
        self.returnStageOneButton.setGeometry(QtCore.QRect(800, 680, 101, 23))
        self.returnStageOneButton.setObjectName("returnStageOneButton")
        self.filterToolPlotTable_2 = filterToolPlotStage2(self.stageTwo)
        self.filterToolPlotTable_2.setGeometry(QtCore.QRect(330, 30, 550, 381))
        self.filterToolPlotTable_2.setObjectName("filterToolPlotTable_2")
        self.parametersInfoLabel = QtWidgets.QLabel(self.stageTwo)
        self.parametersInfoLabel.setGeometry(QtCore.QRect(450, 480, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.parametersInfoLabel.setFont(font)
        self.parametersInfoLabel.setObjectName("parametersInfoLabel")
        self.parametersInfoLabel_2 = QtWidgets.QLabel(self.stageTwo)
        self.parametersInfoLabel_2.setGeometry(QtCore.QRect(50, 60, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.parametersInfoLabel_2.setFont(font)
        self.parametersInfoLabel_2.setObjectName("parametersInfoLabel_2")
        self.widget_3 = QtWidgets.QWidget(self.stageTwo)
        self.widget_3.setGeometry(QtCore.QRect(10, 90, 301, 301))
        self.widget_3.setObjectName("widget_3")
        self.plotTypeOptionInput_2 = QtWidgets.QComboBox(self.stageTwo)
        self.plotTypeOptionInput_2.setGeometry(QtCore.QRect(490, 440, 301, 21))
        self.plotTypeOptionInput_2.setObjectName("plotTypeOptionInput_2")
        self.plotTypeOptionInput_2.addItem("")
        self.plotTypeOptionInput_2.addItem("")
        self.plotTypeOptionInput_2.addItem("")
        self.plotTypeOptionLabel_2 = QtWidgets.QLabel(self.stageTwo)
        self.plotTypeOptionLabel_2.setGeometry(QtCore.QRect(450, 440, 31, 16))
        self.plotTypeOptionLabel_2.setObjectName("plotTypeOptionLabel_2")
        self.hsLabelNum_4 = QtWidgets.QLabel(self.stageTwo)
        self.hsLabelNum_4.setGeometry(QtCore.QRect(420, 620, 461, 16))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.hsLabelNum_4.setFont(font)
        self.hsLabelNum_4.setObjectName("hsLabelNum_4")
        self.hsLabel_2 = QtWidgets.QLabel(self.stageTwo)
        self.hsLabel_2.setGeometry(QtCore.QRect(360, 610, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hsLabel_2.setFont(font)
        self.hsLabel_2.setObjectName("hsLabel_2")
        self.hsLabelDen_2 = QtWidgets.QLabel(self.stageTwo)
        self.hsLabelDen_2.setGeometry(QtCore.QRect(420, 630, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hsLabelDen_2.setFont(font)
        self.hsLabelDen_2.setText("")
        self.hsLabelDen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hsLabelDen_2.setObjectName("hsLabelDen_2")
        self.hsLabelNum_2 = QtWidgets.QLabel(self.stageTwo)
        self.hsLabelNum_2.setGeometry(QtCore.QRect(420, 610, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hsLabelNum_2.setFont(font)
        self.hsLabelNum_2.setText("")
        self.hsLabelNum_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hsLabelNum_2.setObjectName("hsLabelNum_2")
        self.splitInSos = QtWidgets.QCheckBox(self.stageTwo)
        self.splitInSos.setGeometry(QtCore.QRect(70, 400, 171, 17))
        self.splitInSos.setObjectName("splitInSos")
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
        self.hiddenWidget.setCurrentIndex(0)
        self.hiddenWarning.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(filterToolWindow)

    def retranslateUi(self, filterToolWindow):
        _translate = QtCore.QCoreApplication.translate
        filterToolWindow.setWindowTitle(_translate("filterToolWindow", "MainWindow"))
        self.filterTypeOption.setItemText(0, _translate("filterToolWindow", "Low-Pass"))
        self.filterTypeOption.setItemText(1, _translate("filterToolWindow", "High-Pass"))
        self.filterTypeOption.setItemText(2, _translate("filterToolWindow", "Band-Pass"))
        self.filterTypeOption.setItemText(3, _translate("filterToolWindow", "Band-Rejection"))
        self.filterTypeOption.setItemText(4, _translate("filterToolWindow", "Group Delay"))
        self.approxTypeOption.setItemText(0, _translate("filterToolWindow", "Butterworth"))
        self.approxTypeOption.setItemText(1, _translate("filterToolWindow", "Cauer"))
        self.approxTypeOption.setItemText(2, _translate("filterToolWindow", "Cheby1"))
        self.approxTypeOption.setItemText(3, _translate("filterToolWindow", "Cheby2"))
        self.approxTypeOption.setItemText(4, _translate("filterToolWindow", "Legendre"))
        self.filterTypeOptionLabel.setText(_translate("filterToolWindow", "Filter Type"))
        self.aproxTypeOptionLabel.setText(_translate("filterToolWindow", "Approximation"))
        self.filterTypeOptionLabel_2.setText(_translate("filterToolWindow", "Filter Parameters"))
        self.wrgLabel.setText(_translate("filterToolWindow", "Wrg [rad/s] "))
        self.tolLabel.setText(_translate("filterToolWindow", "Tolerance [%] "))
        self.tauLabel.setText(_translate("filterToolWindow", "Tau [ms] "))
        self.aaLabel.setText(_translate("filterToolWindow", "Aa [DB] "))
        self.apLabel.setText(_translate("filterToolWindow", "Ap [DB] "))
        self.faLabel.setText(_translate("filterToolWindow", "fa [Hz] "))
        self.fpLabel.setText(_translate("filterToolWindow", "fp [Hz] "))
        self.famLabel.setText(_translate("filterToolWindow", " faM[Hz] "))
        self.fpmLabel.setText(_translate("filterToolWindow", "fpM [HZ] "))
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
        self.plotTypeOptionLabel.setText(_translate("filterToolWindow", "Plot"))
        self.acceptParametersStageOne.setText(_translate("filterToolWindow", "Add Filter"))
        self.filterDesignedLabel.setText(_translate("filterToolWindow", "Filters"))
        self.plotAllCheckBox.setText(_translate("filterToolWindow", "Plot All"))
        self.hsLabel.setText(_translate("filterToolWindow", "H(S)="))
        self.hsLabelNum_3.setText(_translate("filterToolWindow", "______________________________________________________________________________________________________________________________________________________"))
        self.okToRemove.setText(_translate("filterToolWindow", "✔"))
        self.noOkToRemove.setText(_translate("filterToolWindow", "x"))
        self.label_3.setText(_translate("filterToolWindow", "Changing the parameters"))
        self.label_4.setText(_translate("filterToolWindow", "of the template will remove"))
        self.label_5.setText(_translate("filterToolWindow", "all previous filters. Do you"))
        self.label_6.setText(_translate("filterToolWindow", "want to proceed?"))
        self.label_2.setText(_translate("filterToolWindow", "Stage 2"))
        self.returnStageOneButton.setText(_translate("filterToolWindow", "Return to Stage 1"))
        self.parametersInfoLabel.setText(_translate("filterToolWindow", "Filter Parameters"))
        self.parametersInfoLabel_2.setText(_translate("filterToolWindow", "Transfer Functions"))
        self.plotTypeOptionInput_2.setItemText(0, _translate("filterToolWindow", "Magnitude"))
        self.plotTypeOptionInput_2.setItemText(1, _translate("filterToolWindow", "Phase"))
        self.plotTypeOptionInput_2.setItemText(2, _translate("filterToolWindow", "Poles and Zeros"))
        self.plotTypeOptionLabel_2.setText(_translate("filterToolWindow", "Plot"))
        self.hsLabelNum_4.setText(_translate("filterToolWindow", "______________________________________________________________________________________________________________________________________________________"))
        self.hsLabel_2.setText(_translate("filterToolWindow", "H(S)="))
        self.splitInSos.setText(_translate("filterToolWindow", "Split in Second Orden System"))
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
