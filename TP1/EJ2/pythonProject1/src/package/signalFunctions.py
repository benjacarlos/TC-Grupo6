
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

import src.package.bodeFunctions as bode



class sgList():

    def __init__(self):

        self.signalList = []

    def addSignalList(self, function):
        self.signalList.append(function)
        print(self.signalList)

    def removeSignalList(self, function):
        self.signalList.remove(function)




class SignalResponse():

    def __init__(self):

        self.bodes = bode.bodes()
        self.sgl = sgList()

    def sine(self, amp, freq, phase, DClevel):

        print(self.bodes.transferFunctionList)

        #for x in self.bodes.transferFunctionList:
            #print(x)
        num = [1] #self.bodes.transFuncList[0]
        denom = [1,1,1] #self.bodes.transFuncList[1]
        x = (num, denom)
        self.t = np.linspace(0, 1, num = 1000)
        self.u = amp*np.sin(2*np.pi*freq*self.t + np.radians(phase)) + DClevel
        self.tout, self.yout, self.xout = signal.lsim(x, U = self.u, T = self.t) 
        self.sgl.addSignalList((self.t, self.u, self.t, self.yout))

#        num = [1] #self.bodes.transFuncList[0]
#        denom = [1,1,1] #self.bodes.transFuncList[1]
#        self.H = signal.TransferFunction(num, denom)
#        self.t = np.linspace(0, 1, num = 1000)



    def step(self, amp):

        for x in self.bodes.transferFunctionList:
            self.t, self.yout = signal.step(x)
            self.u = amp * heaviside(self.t, 0.5)
            self.yout *= amp 
            self.sgl.addSignalList((self.t, self.u, self.t, self.yout))

    def square(self, amp, freq, duty, DClevel):

        for x in self.bodes.transferFunctionList:
            self.t = np.linspace(0, 1, num = 1000)
            self.u = amp * signal.square(2*np.pi*freq*self.t, duty/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(x, U = self.u, T = self.t)
            self.sgl.addSignalList((self.t, self.u, self.tout, self.yout))

    def impulse(self, amp, freq, phase):
        pass

    def triangle(self, amp, freq, phase, symmetry):
        for x in self.bodes.transferFunctionList:
            self.t = np.linspace(0, 1, num = 1000)
            self.u = amp * signal.sawtooth(2*np.pi*freq*self.t, symetry/100) + DClevel
            self.tout, self.yout, self.xout = signal.lsim(x, U = self.u, T = self.t)
            self.sgl.addSignalList((self.t, self.u, self.tout, self.yout))

    






