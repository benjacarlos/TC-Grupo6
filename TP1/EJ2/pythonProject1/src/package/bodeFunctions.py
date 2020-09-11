import numpy as np
from scipy import signal


#############################################
# Funcionalidad:                            #
# - Clase Principal para los BODEs indepen- #
#   temente de su INPUT                     #
#############################################

class bodes():
    def __init__(self):

        # Lista que contiene cada elemento de tipo BODE#
        self.bodesList = []
        self.transferFunctionList = []
        self.colors_ = "bgrcmykw"
        self.color_index = 0

    def addBodePlot (self,bodePlot):
        self.bodesList.append(bodePlot)

    def removeBodePlot(self,bodePlot):
        self.bodesList.remove(bodePlot)


    def __read_file_ltspice__(self, lines):

        data = dict()

        data["w"] = []
        data["mag"] = []
        data["phase"] = []

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

    def __read_file_ltspice__from_wf(self, lines):

        data = dict()

        data["w"] = []
        data["mag"] = []
        data["phase"] = []

        for i in range(1, len(lines)):
            pnt = 0
            c1 = ""
            c2 = ""
            c3 = ""
            while lines[i][pnt] != '\t':
                c1 += lines[i][pnt]
                pnt += 1

            while self.__not_num__(lines[i][pnt]):
                if lines[i][pnt] == 'n':
                    return data
                pnt += 1

            while lines[i][pnt] != '\t':
                c2 += lines[i][pnt]
                pnt += 1



            while self.__not_num__(lines[i][pnt]):
                pnt += 1

            while lines[i][pnt] != '\n':
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
        try:
            data = self.__read_file_ltspice__(lines)
        except:
            data = self.__read_file_ltspice__from_wf(lines)
        return data

#############################################
# Funcionalidad:                            #
# - Clase Principal un BODE                 #
#   Cada BODE tiene asociado de dónde pro-  #
#   viene y w, fase y magnitud              #
#   Además contiene la definición de si debe#
#   ser graficado o no.                     #
#############################################

class bodeFunction:

    def __init__(self, mode, data, transferNumerator, transferDenominator):
        self.bodeGraph = True
        self.color= None

        # Según cada input se crea el BODE para que sea consistente independientemente del tipo #

        if mode =="key_values":
            self.transferFunction = signal.TransferFunction(transferNumerator, transferDenominator)
            self.transferNumerator = transferNumerator
            self.transferDenominator = transferDenominator

            # Returns
            # w 1D ndarray
            # Frequency array [rad/s]
            #
            # mag 1D ndarray
            # Magnitude array [dB]
            #
            # phase 1D ndarray
            # Phase array [deg]
            m = np.linspace(10e1, 10e8, 1000000)
            self.w, self.mag, self.phase = signal.bode(self.transferFunction, w=m)

            # self.w, self.mag, self.phase = signal.bode(self.transferFunction)
            self.bodeType = "transferFunction"


        if mode=="ltspice":
            self.w, self.mag, self.phase = data["w"], data["mag"] , data["phase"]
            self.bodeType = "spiceFunction"

        if mode=="mesaured_values":
            self.mag = np.asarray(data['MAG'])
            self.w = np.asarray(data['frequency'])
            self.phase = np.asarray(data['PHA'])
            self.bodeType = "csvFunction"



