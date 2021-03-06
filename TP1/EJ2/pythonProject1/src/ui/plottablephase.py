from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

#############################################
# Funcionalidad:                            #
# - Clase Principal el gráfico de FASE      #
#############################################

class plotTablePhase(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(self.toolbar)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.title.set_text ('Diagrama de BODE - FASE')
        self.setLayout(vertical_layout)
