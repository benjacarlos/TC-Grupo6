#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellip.html#scipy.signal.ellip
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellipord.html#scipy.signal.ellipord
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch

class gaussFilter ():
    def __init__(self, A_p,A_a,w_p,w_a,w_max):
        self.A_p=A_p
        self.A_a=A_a
        self.w_p=w_p
        self.w_a=w_a
        self.w_max=w_max
        self.n,self.fc=signal.ellipord(w_p,w_a,A_p,A_a,analog=True)
        self.b,self.a=signal.ellip(self.n,self.A_p,self.A_a,self.fc,'lowpass',analog=True,output='ba')
        self.w,self.h=signal.freqs(self.b, self.a, worN=np.linspace(0, self.w_max, 1000))
        self.magnitudeh = 20 * np.log10(abs(self.h))