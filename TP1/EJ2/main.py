import time

from scipy import signal
import matplotlib.pyplot as plt

class bodePlots():
    def __init__(self):
        self.bodePlotsList = []
        plt.figure("bodeGain")
        plt.figure("bodePhase")

    def addBodePlot (self,bodePlot):
        self.bodePlotsList.append(bodePlot)

    def removeBodePlot(self,bodePlot):
        self.bodePlotsList.remove(bodePlot)

    def updatePlot (self):
        plt.figure("bodeGain")
        plt.semilogx(self.bodePlotsList[-1].w, self.bodePlotsList[-1].mag)
        plt.figure("bodePhase")
        plt.semilogx(self.bodePlotsList[-1].w, self.bodePlotsList[-1].phase)
        plt.draw()
        plt.show()


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

#####################################################################################################
# transferNumerator is a list which represents the values of each polynomial coefficient of NUM     #
# transferDenominator is a list which represents the values of each polynomial coefficient of DEN   #
# Transfer Function is represented by H(S) = NUM (S)/ DEN (S)                                       #
# e.g. s^2 + 3s + 5 would be represented as [1, 3, 5]                                               #
#####################################################################################################

def bodePlotter(transferNumerator, transferDenominator):
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html

    transferFunction = signal.TransferFunction(transferNumerator, transferDenominator)
    w, mag, phase = signal.bode(transferFunction)

    transferNumerator2 = [1,1,1]
    transferDenominator2 = [1, 1]
    transferFunction2 = signal.TransferFunction(transferNumerator2, transferDenominator2)
    w2, mag2, phase2 = signal.bode(transferFunction2)
    plt.ion()
    plt.figure(1)
    plt.semilogx(w, mag)  # Bode magnitude plot
    #plt.semilogx(w2, mag2)
    plt.xlabel('Decades')
    plt.ylabel('Gain (Db)')
    plt.figure(num="PHASE")
    plt.semilogx(w, phase)  # Bode phase plot
    plt.xlabel('Angular Frequency')
    plt.ylabel('Phase (Degree)')
    #plt.show() This is a blocking function.

    plt.draw()

    plt.figure(1)
    plt.semilogx(w2, mag2)


def main():
    #plt.ion()
    END = False
    myBodePlots = bodePlots()
    transferNumerator = [1]
    transferDenominator = [1, 1]

    transferNumerator2 = [2]
    transferDenominator2 = [3, 1]
    myFirstBode = bodeFunction(transferNumerator, transferDenominator)
    mySecondBode = bodeFunction(transferNumerator2, transferDenominator2)

    myBodePlots.addBodePlot(myFirstBode)
    myBodePlots.updatePlot()
    #plt.show()

    #while (END == False):
    #   plt.pause(0.00001)

    myBodePlots.addBodePlot(mySecondBode)
    myBodePlots.updatePlot()
if __name__ == '__main__':
    main()








#############################################
# plt.draw () not working
# After some research
#https://stackoverflow.com/questions/35215335/matplotlibs-ion-and-draw-not-working
# The problem - and the solution - is highly dependent on the plot.draw() function within the Python environment and back end, and may even vary in different product releases. It manifests itself in different ways depending on the environment. The problem shows up in many places on stackoverflow with some solutions working for some people and not for others.
#
# The gold standard on my Windows laptop is running the Python from the command line - no IDE, just plain vanilla Python3. draw() as shown in the example always works fine there.
#
# If I try it in Jupyter notebook on the same machine, no amount of draw(), plot.pause(), plot.show(), or any other suggestion works. I tried %matplotlib with notebook, widget and ipympl. Nothing gets drawn until complete end of cell code execution.
#
# Some other sources on stackoverflow suggested using figure.canvas.flush_events(). I had some success with that and investigated further.
#
# The best solution turned out to be to run the draw() at the figure.canvas level instead of the axes or plot level.


