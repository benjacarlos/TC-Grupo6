import sympy
import math
from scipy import signal
import numpy as np
from numpy.polynomial import polynomial as pol
from numpy import roots
import matplotlib.pyplot as plt
from numpy import pi, diff, unwrap, angle


def gaussFilter(A_p, A_a, w_p, w_a, w_max, n,wrg,tol,tau):

    # El range va de 1 a n-1#
    nMax = n + 1
    myGaussSum = 0
    imNumber = sympy.I
    s = sympy.symbols("s")
    wrg_norm = wrg*tau
    tau_norm = 1

    # Itero hasta llegar al mejor N#
    for k in range(1, nMax):
        # Defino la Sumatoria del Denominador de una Gaussiana#


        ###ACA ES 1 o -1?
        myGaussSum += (((1) ** k) / (math.factorial(k)) * (s / imNumber) ** (2 * k))

    rawGaussFilter = 1 / (1 + myGaussSum)

    # De la expresion obtengo

    rawGaussFilterNum,rawGaussFilterDen = sympy.fraction(rawGaussFilter)

    rawGaussFilterNumInCoeff = sympy.Poly(rawGaussFilterNum,s).all_coeffs()
    rawGaussFilterDenInCoeff = sympy.Poly(rawGaussFilterDen,s).all_coeffs()

    poles = np.poly1d(rawGaussFilterDenInCoeff)

    gaussFilterPoles = []

    for pole in roots(poles):
        if pole.real < 0:
            gaussFilterPoles.append(pole.real)


    myDenominator = pol.polyfromroots(gaussFilterPoles)

    print (myDenominator)

    #######################################################
    # Evaluo retardo de grupo
    #

    w,h = signal.freqs([1], myDenominator)

    w, gd = signal.group_delay((w, h))


    plt.figure()
    plt.plot(w,gd)
    plt.show()

    #if (gd[wrg_norm])

    return [1],myDenominator
    #########################################

if __name__ == '__main__':

    A_a=30
    A_p=3
    w_p=100e3
    w_a=150e3
    w_max=1e6
    wrg = 600
    tol=20
    tau = 10e-3


    #n=1
    num,den =gaussFilter(A_p,A_a,w_p,w_a,w_max,2,wrg,tol,tau)
    num2, den2 = gaussFilter(A_p, A_a, w_p, w_a, w_max, 2,wrg,tol,tau)

    system = signal.TransferFunction (num,den)
    system2 = signal.TransferFunction(num2, den2)
    w,mag,phase = signal.bode(system)
    w2,mag2,phase2 = signal.bode(system2)
    plt.figure()
    plt.semilogx(w, mag)
    plt.semilogx(w2,mag2)
    lti = signal.lti(num2,den2)
    plt.figure()
    x,y = signal.impulse (lti)
    plt.plot(x, y)

    plt.figure()
    wn,t = signal.group_delay((num2,den2))
    plt.plot (wn,t)
    plt.show()
