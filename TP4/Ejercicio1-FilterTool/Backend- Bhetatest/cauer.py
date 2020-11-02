#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellip.html#scipy.signal.ellip
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellipord.html#scipy.signal.ellipord
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch


def cauer(A_p,A_a,w_p,w_a,w_max):

    [n,fc]=signal.ellipord(w_p,w_a,A_p,A_a,analog=True)

    [b,a]=signal.ellip(n,A_p,A_a,fc,'lowpass',analog=True,output='ba')

    w, h = signal.freqs(b, a, worN=np.linspace(0, w_max, 1000))
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title('Elliptic filter frequency response (rp=5, rs=40)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    #plt.axvline(fc, color='green')  # cutoff frequency
    #plt.axvline(w_a, color='red')  # cutoff frequency
    #plt.axvline(w_p, color='red')  # cutoff frequency

    #plt.axhline(-A_a, color='green')  # rs
    #plt.axhline(-A_p, color='green')  # rp
    #plt.plot([0, fc], [-A_p, -A_p], color='green', alpha=0.8)
    bb = mtransforms.Bbox([[0, 0], [fc, w_max]])
    plt.tight_layout()
    rectangle_p = plt.Rectangle((0, -A_p), fc, -A_a-100, fc='violet', alpha=0.8)
    rectangle_a = plt.Rectangle((w_a, -A_a), w_max-fc, A_a+30, fc='violet', alpha=0.8)

    plt.gca().add_patch(rectangle_p)
    plt.gca().add_patch(rectangle_a)


    plt.show()

    print(n)
