
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

import src.package.bodeFunctions as bode



class sgList():

    def __init__(self):

        self.signalList = []

    def addSignalList(self, function):
        self.signalList.append(function)

    def removeSignalList(self, function):
        self.signalList.remove(function)




class SignalResponse():

    def __init__(self, mode, H, amp, freq, phase, DClevel, DutyOrSym, tf, labelH):

        self.signalGraph = True
        self.plotCheck = True

        if mode == "sine":
            self.t = np.linspace(0, tf, 2000, dtype='float64')
            self.u = amp*np.sin(2*np.pi*freq*self.t + np.radians(phase)) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t) 
            self.signalType = "senoidal"
            self.labelH = labelH

        if mode == "step":
            self.t = np.linspace(0, tf, 2000, dtype='float64')
            self.u = amp * np.heaviside(self.t, 0.5)
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "escalón"
            self.labelH = labelH

        if mode == "square":

            self.t = np.linspace(0, tf, 2000, dtype='float64')
            self.u = amp * signal.square(2*np.pi*freq*self.t, DutyOrSym/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "cuadrada"
            self.labelH = labelH

        if mode == "impulse":
            self.t = np.linspace(0, tf, 2000, dtype='float64')
            self.u = amp * signal.unit_impulse(2000, None)
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "impulso"
            self.labelH = labelH

        if mode == "triangle":
            self.t = np.linspace(0, tf, 2000, dtype='float64')
            self.u = amp * signal.sawtooth(2*np.pi*freq*self.t, DutyOrSym/100) + DClevel
            print(self.u)
            print('\n')
            print('AAAAAAAAAAAAAAAAAA')
            print('\n')
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            print(self.yout)
            print('\n')
            print('AAAAAAAAAAAAAAAAAA')
            print('\n')
            self.signalType = "triangular"
            print(self.signalType)
            print('\n')
            print('AAAAAAAAAAAAAAAAAA')
            print('\n')
            self.labelH = labelH

    






