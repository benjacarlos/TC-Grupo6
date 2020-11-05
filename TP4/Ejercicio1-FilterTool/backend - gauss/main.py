import sympy
from sympy import atan,im,re
import math
from scipy import signal
import numpy as np
from numpy.polynomial import polynomial as pol
from numpy import roots
import matplotlib.pyplot as plt
from numpy import pi, diff, unwrap, angle
from numpy import pi, log10, abs, logspace, diff, unwrap, angle


##############################################
# Esta funcion devuelve el filtro Gaussiano  #
# en polos y zeros, H(S) y H(jw)             #
##############################################

def gaussFilter(A_p, A_a, w_p, w_a, w_max, n,wrg,tol,tau):

    # El range va de 1 a n-1#

    nMax = n + 1
    myGaussSum = 0
    imNumber = sympy.I
    s = sympy.symbols("s")
    w = sympy.symbols("w")
    wrg_norm = wrg*tau
    tau_norm = 1

    # Itero hasta llegar al mejor N#

    for k in range(1, nMax):
        # Defino la Sumatoria del Denominador de una Gaussiana#

        myGaussSum += (((-1) ** k) / (math.factorial(k)) * (s) ** (2 * k))

    rawGaussFilter = 1 / (1 + myGaussSum)

    #FUNCION GAUSSIANA CRUDA#
    #print("ACA TENGO LA FUNCION GAUSSIANA CRUDA:")
    #print (rawGaussFilter)

    # Separo en denominador y numerador #
    rawGaussFilterNum,rawGaussFilterDen = sympy.fraction(rawGaussFilter)


    # Transformo el polinomio obtenido en [coefMax,...,coefMin]

    rawGaussFilterDenInCoeff = sympy.Poly(rawGaussFilterDen,s).all_coeffs()

    # COEFICIENTE DE MI DENOMINADOR#
    #print ("ACA TENGO EL COEFICIENTE DE MI DENOMINADOR:")
    #print (rawGaussFilterDenInCoeff)

    #print("ACA TENGO TODOS LOS POLOS:")
    poles = np.poly1d(rawGaussFilterDenInCoeff)

    #print (roots(poles))

    gaussFilterPoles = []

    # Filtro las raices con parte real negativa

    for pole in roots(poles):
        if pole.real < 0:
            gaussFilterPoles.append(pole)

    # Esta funcion me devuelve el polinomio en un array en el orden a+bx**1+c**2+...+d**n

    myDenominator = pol.polyfromroots(gaussFilterPoles)

    #######################################################
    # Evaluo retardo de grupo
    #

    # Retorno el numerador que siempre es 1
    # Retorno la parte real de los coeficientes del denominador ya que por aproximacion de la libreria
    # hay parte imaginaria para ordenes mayores a 5 que son muy muy pequeños :(

    num = [1]
    den = myDenominator.real[::-1]
    for i in range (0,len(den)):
        coeff = coeff * (tau)**(len(den))


    w,h = signal.freqs([1],myDenominator.real[::-1])
    group_delay = -np.diff(np.unwrap(np.angle(h))) / np.diff(w)

    return [1],myDenominator.real[::-1],[],gaussFilterPoles,group_delay,w[1:]

    #########################################

def createPolynomialInSymbolFromRoots(roots):

    w = sympy.symbols('w')
    whole =1
    for root in roots:
        whole *=(sympy.I*w-root)
    return(whole.expand())

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
    num,den,myZeros,myPoles,gd,wd = gaussFilter(A_p,A_a,w_p,w_a,w_max,2,wrg,tol,tau)
    num2, den2, myZeros2, myPoles2, gd2, wd2 = gaussFilter(A_p, A_a, w_p, w_a, w_max, 4, wrg, tol, tau)
    num3, den3, myZeros3, myPoles3, gd3, wd3 = gaussFilter(A_p, A_a, w_p, w_a, w_max, 15, wrg, tol, tau)
    print (myPoles)

    system = signal.TransferFunction (num,den)

    w,mag,phase = signal.bode(system)


    #plt.figure()

    #plt.semilogx(w, mag)

    #plt.show()

    plt.figure()
    plt.semilogx (wd,gd)
    plt.semilogx(wd2, gd2)
    plt.semilogx(wd3, gd3)

    plt.show()