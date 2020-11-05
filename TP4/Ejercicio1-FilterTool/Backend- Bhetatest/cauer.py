#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellip.html#scipy.signal.ellip
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellipord.html#scipy.signal.ellipord
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch


def cauer(A_p,A_a,w_p,w_a,n_hardcodeado,cte_des):

    n,fc=signal.ellipord(w_p,w_a,A_p,A_a,analog=True)

    if n_hardcodeado != 0:
        n=n_hardcodeado

    z,p,k=signal.ellip(n,A_p,A_a,w_p,'lowpass',analog=True,output='zpk')

    return z,p,k,n
    # w, h = signal.freqs(b, a, worN=np.linspace(0, w_max, 1000))
    # plt.semilogx(w, 20 * np.log10(abs(h)))
    # plt.title('Elliptic filter frequency response (rp=5, rs=40)')
    # plt.xlabel('Frequency [radians / second]')
    # plt.ylabel('Amplitude [dB]')
    # plt.margins(0, 0.1)
    # plt.grid(which='both', axis='both')
    # #plt.axvline(fc, color='green')  # cutoff frequency
    # #plt.axvline(w_a, color='red')  # cutoff frequency
    # #plt.axvline(w_p, color='red')  # cutoff frequency
    #
    # #plt.axhline(-A_a, color='green')  # rs
    # #plt.axhline(-A_p, color='green')  # rp
    # #plt.plot([0, fc], [-A_p, -A_p], color='green', alpha=0.8)
    #
    #
    #
    # plt.show()

