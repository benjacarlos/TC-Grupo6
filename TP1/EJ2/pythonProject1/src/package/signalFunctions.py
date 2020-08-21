
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

import src.package.bodeFunctions as bode



    #########################################################################

    #############################################
    # Funcionalidad:                            #
    # - Gestiona lista que contiene las señales #
    #   introducidas y la respuesta de los      #
    #   sistemas a las mismas.                  #
    #############################################


class sgList():

    def __init__(self):

        #Lista que contiene cada elemento de tipo Signal#

        self.signalList = []

    def addSignalList(self, function):
        self.signalList.append(function)

    def removeSignalList(self, function):
        self.signalList.remove(function)


    #########################################################################

    #############################################
    # Funcionalidad:                            #
    # - Cálculo de las señales introducidas y   #
    #   la respuesta de los sistemas.           #
    #############################################

class SignalResponse():

    def __init__(self, mode, H, amp, freq, phase, DClevel, DutyOrSym, tf, labelH, timeUnit, freqUnit):

        self.signalGraph = True
        self.plotCheck = True
        self.color= None


        #Cálculo señal senoidal#

        if mode == "sine":
            
            t = self.checkTimeUnit(tf, timeUnit)
            f = self.checkFreqUnit(freq, freqUnit)
            self.t = np.linspace(0, t, 10000, dtype='float64')
            self.u = amp*np.sin(2*np.pi*f*self.t + np.radians(phase)) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t) 
            self.signalType = "senoidal"
            self.labelH = labelH


        #Cálculo señal escalón y la respuesta del sistema#

        if mode == "step":

            t = self.checkTimeUnit(tf, timeUnit)
            self.t = np.linspace(0, tf, 3000, dtype='float64')
            self.u = amp * np.heaviside(self.t, 0.5)
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "escalón"
            self.labelH = labelH


        #Cálculo de señal cuadrada y la respuesta del sistema#

        if mode == "square":

            t = self.checkTimeUnit(tf, timeUnit)
            f = self.checkFreqUnit(freq, freqUnit)
            self.t = np.linspace(0, t, 1000, dtype='float64')
            self.u = amp * signal.square(2*np.pi*f*self.t, DutyOrSym/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "cuadrada"
            self.labelH = labelH

        #Cálculo del impulso y respuesta impulsiva#

        if mode == "impulse":

            t = self.checkTimeUnit(tf, timeUnit)
            self.t = np.linspace(0, tf, 2000, dtype='float64')
            self.u = amp * signal.unit_impulse(2000, None)
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "impulso"
            self.labelH = labelH

        #Cálculo señal triangular y la respuesta del sistema#

        if mode == "triangle":
            
            t = self.checkTimeUnit(tf, timeUnit)
            f = self.checkFreqUnit(freq, freqUnit)
            self.t = np.linspace(0, t, 10000, dtype='float64')
            self.u = amp * signal.sawtooth(2*np.pi*f*self.t, DutyOrSym/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "triangular"
            print(self.signalType)
            self.labelH = labelH

    #############################################
    # Funcionalidad:                            #
    # - Validación y pasaje de unidades elegidas#
    #############################################


    def checkTimeUnit(self, tf, timeUnit):
        if timeUnit == "s":
            return tf
        elif timeUnit == "ms":
            return tf* 1e-3
        elif timeUnit == "us":
            return tf* 1e-6
        elif timeUnit == "ns":
            return tf* 1e-9

    def checkFreqUnit(self, freq, freqUnit):
        if freqUnit == "Hz":
            return freq
        elif freqUnit == "kHz":
            return (freq * 1e3)
        elif freqUnit == "MHz":
            return freq* 1e6
        elif freqUnit == "GHz":
            return freq* 1e9

    






