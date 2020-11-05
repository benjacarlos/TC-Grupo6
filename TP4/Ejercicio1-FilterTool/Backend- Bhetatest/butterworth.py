#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellip.html#scipy.signal.ellip
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ellipord.html#scipy.signal.ellipord
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch


def butterworth(A_p,A_a,w_p,w_a,n_hardcodeado,cte_des):

    n,fc=signal.ellipord(w_p,w_a,A_p,A_a,analog=True)

    if n_hardcodeado != 0:
        n=n_hardcodeado

    z,p,gain=signal.ellip(n,A_p,A_a,w_p,'lowpass',analog=True,output='zpk')
    num, den = signal.zpk2tf(z, p, gain)

    #Proceso de desnormalizacion
    if cte_des != 0:  #Busco la frecuencia a la cual estoy en Aa con una estimación
        k = 1 / w_a
        w, h = signal.freqs(num, den, worN=np.linspace(1, w_a, 1000))
        array = np.abs(np.asarray(20 * np.log10(abs(h))))
        idx = (np.abs(array - A_a)).argmin()
        w_a_prima=w[idx]
        A_a_detec=array[idx]
        w_p_prima=w_p+(w_a-w_a_prima)
        print(w_a_prima)

        n, fc = signal.ellipord(w_p_prima, w_a, A_p, A_a, analog=True)

        if n_hardcodeado != 0:
            n = n_hardcodeado

        z, p, gain = signal.ellip(n, A_p, A_a, w_p_prima, 'lowpass', analog=True, output='zpk')

    return z,p,gain,n
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

