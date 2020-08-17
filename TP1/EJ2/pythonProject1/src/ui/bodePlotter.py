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
        bodePlotterWindow.resize(633, 760)
        self.centralwidget = QtWidgets.QWidget(bodePlotterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xLabelText = QtWidgets.QLabel(self.centralwidget)
        self.xLabelText.setGeometry(QtCore.QRect(60, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.xLabelText.setFont(font)
        self.xLabelText.setObjectName("xLabelText")
        self.yLabelText = QtWidgets.QLabel(self.centralwidget)
        self.yLabelText.setGeometry(QtCore.QRect(60, 60, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yLabelText.setFont(font)
        self.yLabelText.setObjectName("yLabelText")
        self.groupTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.groupTextLabel.setGeometry(QtCore.QRect(460, 0, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupTextLabel.setFont(font)
        self.groupTextLabel.setObjectName("groupTextLabel")
        self.plotTablePhase = plotTablePhase(self.centralwidget)
        self.plotTablePhase.setGeometry(QtCore.QRect(280, 430, 651, 381))
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
        self.removePlotsAction.setGeometry(QtCore.QRect(50, 622, 139, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.removePlotsAction.setFont(font)
        self.removePlotsAction.setObjectName("removePlotsAction")
        self.transferFunction = QtWidgets.QStackedWidget(self.centralwidget)
        self.transferFunction.setGeometry(QtCore.QRect(40, 170, 181, 161))
        self.transferFunction.setObjectName("transferFunction")
        self.transferFunctionOption = QtWidgets.QWidget()
        self.transferFunctionOption.setObjectName("transferFunctionOption")
        self.transferFunctionAction = QtWidgets.QPushButton(self.transferFunctionOption)
        self.transferFunctionAction.setGeometry(QtCore.QRect(10, 40, 141, 91))
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
        self.spiceFunction = QtWidgets.QStackedWidget(self.centralwidget)
        self.spiceFunction.setGeometry(QtCore.QRect(20, 360, 191, 101))
        self.spiceFunction.setObjectName("spiceFunction")
        self.spiceOption = QtWidgets.QWidget()
        self.spiceOption.setObjectName("spiceOption")
        self.spiceAction = QtWidgets.QPushButton(self.spiceOption)
        self.spiceAction.setGeometry(QtCore.QRect(30, 10, 139, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spiceAction.setFont(font)
        self.spiceAction.setObjectName("spiceAction")
        self.spiceFunction.addWidget(self.spiceOption)
        self.spiceInput = QtWidgets.QWidget()
        self.spiceInput.setObjectName("spiceInput")
        self.spiceFunctionMsg = QtWidgets.QLabel(self.spiceInput)
        self.spiceFunctionMsg.setGeometry(QtCore.QRect(10, 0, 181, 16))
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
        self.csvAction.setGeometry(QtCore.QRect(20, 20, 139, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.csvAction.setFont(font)
        self.csvAction.setObjectName("csvAction")
        self.csvFunction.addWidget(self.csvOption)
        self.csvInput = QtWidgets.QWidget()
        self.csvInput.setObjectName("csvInput")
        self.csvFunctionMsg = QtWidgets.QLabel(self.csvInput)
        self.csvFunctionMsg.setGeometry(QtCore.QRect(10, 20, 181, 16))
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
        bodePlotterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(bodePlotterWindow)
        self.statusbar.setObjectName("statusbar")
        bodePlotterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(bodePlotterWindow)
        self.transferFunction.setCurrentIndex(0)
        self.spiceFunction.setCurrentIndex(0)
        self.csvFunction.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(bodePlotterWindow)

    def retranslateUi(self, bodePlotterWindow):
        _translate = QtCore.QCoreApplication.translate
        bodePlotterWindow.setWindowTitle(_translate("bodePlotterWindow", "MainWindow"))
        self.xLabelText.setText(_translate("bodePlotterWindow", "Etiqueta EJE X"))
        self.yLabelText.setText(_translate("bodePlotterWindow", "Etiqueta EJE Y"))
        self.groupTextLabel.setText(_translate("bodePlotterWindow", "Plot Tool - Grupo 6"))
        self.phaseUpdateLabel.setText(_translate("bodePlotterWindow", "Φ"))
        self.gainUpdateLabel.setText(_translate("bodePlotterWindow", "| H(jw)|"))
        self.removePlotsAction.setText(_translate("bodePlotterWindow", "Borrar"))
        self.transferFunctionAction.setText(_translate("bodePlotterWindow", "H(S)"))
        self.transferFunctionMsg.setText(_translate("bodePlotterWindow", "Ingrese la Funcion de Transferencia"))
        self.transferFunctionNumLabel.setText(_translate("bodePlotterWindow", "Numerador"))
        self.transferFunctionDenLabel.setText(_translate("bodePlotterWindow", "Denominador"))
        self.saveTransferFunction.setText(_translate("bodePlotterWindow", "Ingresar"))
        self.returnTransferFunction.setText(_translate("bodePlotterWindow", "Volver"))
        self.transferFunctionNameLabel.setText(_translate("bodePlotterWindow", "Nombre"))
        self.spiceAction.setText(_translate("bodePlotterWindow", "SPICE"))
        self.spiceFunctionMsg.setText(_translate("bodePlotterWindow", "Seleccione el archivo de LTSpice"))
        self.saveSpiceFunction.setText(_translate("bodePlotterWindow", "Buscar"))
        self.returnSpiceFunction.setText(_translate("bodePlotterWindow", "Volver"))
        self.label.setText(_translate("bodePlotterWindow", "Nombre"))
        self.csvAction.setText(_translate("bodePlotterWindow", "Medición"))
        self.csvFunctionMsg.setText(_translate("bodePlotterWindow", "Seleccione el archivo con las mediciones"))
        self.saveCsvFunction.setText(_translate("bodePlotterWindow", "Buscar"))
        self.returnCsvFunction.setText(_translate("bodePlotterWindow", "Volver"))
        self.label_2.setText(_translate("bodePlotterWindow", "Nombre"))
from src.ui.plottablegain import plotTableGain
from src.ui.plottablephase import plotTablePhase


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bodePlotterWindow = QtWidgets.QMainWindow()
    ui = Ui_bodePlotterWindow()
    ui.setupUi(bodePlotterWindow)
    bodePlotterWindow.show()
    sys.exit(app.exec_())
