# import time

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt



class bodes():
    def __init__(self):
        self.bodesList = []
        self.transferFunctionList = []
        self.colors_ = "bgrcmykw"
        self.color_index = 0
        plt.figure("bodeGain")
        plt.figure("bodePhase")
        plt.ion()

    def addBodePlot (self,bodePlot):
        self.bodesList.append(bodePlot)

    def removeBodePlot(self,bodePlot):
        self.bodesList.remove(bodePlot)

    def addTransferFunction (self,transferFunction):
        self.transferFunctionList.append(transferFunction)


    def removeTransferFunction (self,transferFunction):
        self.transferFunctionList.remove(transferFunction)

    def updatePlot (self):
        plt.figure("bodeGain")
        plt.semilogx(self.bodesList[-1].w, self.bodesList[-1].mag)
        plt.figure("bodePhase")
        plt.semilogx(self.bodesList[-1].w, self.bodesList[-1].phase)
        plt.draw()
        plt.show()

    # def plot_from_CSV(self, data):
    #
    #     plt.figure("bodeGain")
    #     plt.semilogx(data["f"], data["abs"])
    #     plt.figure("bodePhase")
    #     plt.semilogx(data["f"], data["pha"])
    #     plt.draw()
    #     plt.show()

    def __read_file_ltspice__(self, lines):
        # ltspice_file, _ = QFileDialog.getOpenFileName(filter="*.txt")
        # raw_file = open(ltspice_file, 'r')
        # lines = raw_file.readlines()


        data = dict()

        data["w"] = []
        data["mag"] = []
        data["phase"] = []
        # print(lines)

        for i in range(1, len(lines)):
            pnt = 0
            c1 = ""
            c2 = ""
            c3 = ""
            while lines[i][pnt] != '\t':
                c1 += lines[i][pnt]
                pnt += 1

            while self.__not_num__(lines[i][pnt]):
                pnt += 1

            while lines[i][pnt] != 'd':
                c2 += lines[i][pnt]
                pnt += 1
            pnt += 1
            while self.__not_num__(lines[i][pnt]):
                pnt += 1
            while lines[i][pnt] != '°':
                #            if lines[i][pnt]>0:
                c3 += lines[i][pnt]
                pnt += 1

            c1 = float(c1)
            c2 = float(c2)
            c3 = float(c3)
            #       if(c3<360):
            #            c3=c3-360

            data["w"].append(c1)
            data["mag"].append(c2)
            data["phase"].append(c3)

        return data

    def __not_num__(self, content):
        if content == "0":
            return 0
        if content == "1":
            return 0
        if content == "2":
            return 0
        if content == "3":
            return 0
        if content == "4":
            return 0
        if content == "5":
            return 0
        if content == "6":
            return 0
        if content == "7":
            return 0
        if content == "8":
            return 0
        if content == "9":
            return 0
        if content == "-":
            return 0
        return 1

    def plot_from_ltspice(self, lines):
        data = self.__read_file_ltspice__(lines)
        return data

        # self.myBode = (data["f"], data["abs"], data["pha"])
        # self.addBodePlot(self.myBode)
        # self.plot_from_CSV(data)




class bodeFunction:
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html
    def __init__(self, mode, data, transferNumerator, transferDenominator):
        self.bodeGraph = True
        self.color= None
        if mode =="key_values":
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
            self.bodeType = "transferFunction"


        if mode=="ltspice":
            self.w, self.mag, self.phase = data["w"], data["mag"] , data["phase"]
            self.bodeType = "spiceFunction"

        if mode=="mesaured_values":
            self.mag = np.asarray(data['MAG'])
            self.w = np.asarray(data['frequency'])
            self.phase = np.asarray(data['PHA'])
            self.bodeType = "csvFunction"



