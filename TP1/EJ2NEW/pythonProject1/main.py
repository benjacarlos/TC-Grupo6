from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QMainWindow

# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.Qt import pyqtSlot
import src.package.bodeFunctions as bode

from src.ui.bodePlotter import Ui_bodePlotterWindow

# Python Modules
from numpy import *
from random import *


class myPlot(QMainWindow, Ui_bodePlotterWindow):
    def __init__(self):
        super(myPlot, self).__init__()
        self.setupUi(self)
        self.figureGain = Figure()
        self.canvasGain = FigureCanvas(self.figureGain)
        self.axesGain = self.figureGain.add_subplot()
        canvasIndexGain = self.plotTableGain.addWidget(self.canvasGain)
        self.plotTableGain.setCurrentIndex(canvasIndexGain)
        self.figurePhase = Figure()
        self.canvasPhase = FigureCanvas(self.figurePhase)
        self.axesPhase = self.figurePhase.add_subplot()
        canvasIndexPhase = self.plotTablePhase.addWidget(self.canvasPhase)
        self.plotTablePhase.setCurrentIndex(canvasIndexPhase)
        self.transferFunctionAction.clicked.connect(self.on_plot_update)

    @pyqtSlot()
    def on_plot_update(self):

        myBode = bode.bodeFunction([1], [1, 1])
        self.axesGain.clear()
        self.axesPhase.clear()
        self.axesGain.semilogx(myBode.w, myBode.mag)
        self.axesPhase.semilogx(myBode.w, myBode.phase)
        self.canvasGain.draw()
        self.canvasPhase.draw()


if __name__ == "__main__":

    app = QApplication([])
    myMainWindow = QMainWindow()
    widget = myPlot()
    widget.show()
    app.exec()

