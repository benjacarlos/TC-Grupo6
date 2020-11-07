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

