from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch


def cheby1(A_p,A_a,w_p,w_a,n_hardcodeado,cte_des):

    n,fc=signal.cheb1ord(w_p,w_a,A_p,A_a,analog=True)

    if n_hardcodeado != 0:
        n=n_hardcodeado

    z,p,gain=signal.cheby1(n,A_p,fc,'lowpass',analog=True,output='zpk')
    num, den = signal.zpk2tf(z, p, gain)

    print(n)
    #Proceso de desnormalizacion
    if cte_des != 0:  #Busco la frecuencia a la cual estoy en Aa con una estimación
        k = 1 / w_a
        w, h = signal.freqs(num, den, worN=np.linspace(1, w_a, 1000))
        array = np.abs(np.asarray(20 * np.log10(abs(h))))
        idx = (np.abs(array - A_a)).argmin()
        w_a_prima=w[idx]
        A_a_detec=array[idx]
        w_p_prima=w_p+(w_a-w_a_prima)
        print(w_p_prima)

        n, fc = signal.cheb1ord(w_p_prima, w_a, A_p, A_a, analog=True)

        if n_hardcodeado != 0:
            n = n_hardcodeado

        z, p, gain = signal.cheby1(n,A_p, fc, 'lowpass', analog=True, output='zpk')

    return z,p,gain,n


