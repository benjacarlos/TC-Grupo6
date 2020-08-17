
from scipy import signal

class bodes():
    def __init__(self):
        self.bodesList = []

    def addBodePlot (self,bodePlot):
        self.bodesList.append(bodePlot)

    def removeBodePlot(self,bodePlot):
        self.bodesList.remove(bodePlot)


class bodeFunction:
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html
    def __init__(self,transferNumerator, transferDenominator):
        self.transferFunction = signal.TransferFunction(transferNumerator, transferDenominator)
        #signal.bode
        # Returns
        # w 1D ndarray
        # Frequency array [rad/s]
        #
        # mag 1D ndarray
        # Magnitude array [dB]
        #
        # phase 1D ndarray
        # Phase array [deg]

        self.w, self.mag, self.phase = signal.bode(self.transferFunction)

