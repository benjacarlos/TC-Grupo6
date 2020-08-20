
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

import src.package.bodeFunctions as bode



class sgList():

    def __init__(self):

        self.signalList = []

    def addSignalList(self, function):
        self.signalList.append(function)

        #print(self.signalList)
        #print('\n')
        #print('AAAAAAAAAAAAAAAAAAAAAAAA')
        #print('\n')

    def removeSignalList(self, function):
        self.signalList.remove(function)




class SignalResponse():

    def __init__(self, mode, H, amp, freq, phase, DClevel, DutyOrSym, tf):

        self.signalGraph = True
        if mode == "sine":
            self.t = np.linspace(0, tf, tf*200)
            self.u = amp*np.sin(2*np.pi*freq*self.t + np.radians(phase)) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t) 
            self.signalType = "senoidal"

        if mode == "step":
            self.t = np.linspace(0, tf, tf*200)
            self.u = amp * np.heaviside(self.t, 0.5)
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "step"

        if mode == "square":

            self.t = np.linspace(0, tf, tf*200)
            self.u = amp * signal.square(2*np.pi*freq*self.t, DutyOrSym/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "square"

        if mode == "impulse":
            self.t = np.linspace(0, tf, tf*200)
            self.u = amp * signal.unit_impulse((tf-t0)*200, None)
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "impulse"

        if mode == "triangle":
            self.t = np.linspace(0, tf, tf*200)
            self.u = amp * signal.sawtooth(2*np.pi*freq*self.t, DutyOrSym/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(H, U = self.u, T = self.t)
            self.signalType = "triangle"

    






