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

def gaussFilter(A_p, A_a, w_p, w_a, w_max,wrg,tol,tau,n=0):

    tol = tol / 100
    idealN=False

    if n != 0:
        nMax = n + 1
        myGaussSum = 0
        s = sympy. \
            symbols("s")
        w = sympy.symbols("w")

        for k in range(1, nMax):
            # Defino la Sumatoria del Denominador de una Gaussiana#

            myGaussSum += (((-1) ** k) / (math.factorial(k)) * (s) ** (2 * k))

        rawGaussFilter = 1 / (1 + myGaussSum)

        # Separo en denominador y numerador # #ESTO NO ES NECESARIO. Quedo legacy
        rawGaussFilterNum, rawGaussFilterDen = sympy.fraction(rawGaussFilter)

        # Transformo el polinomio obtenido en [coefMax,...,coefMin]

        rawGaussFilterDenInCoeff = sympy.Poly(rawGaussFilterDen, s).all_coeffs()

        # Esto es el poliniomio del denominador contemplando todos los polos

        poles = np.poly1d(rawGaussFilterDenInCoeff)

        gaussFilterPoles = []

        # Filtro las raices con parte real negativa

        for pole in roots(poles):
            if pole.real < 0:
                gaussFilterPoles.append(pole)

        # Esta funcion me devuelve el polinomio en un array en el orden a+bx**1+c**2+...+d**n
        # Tengo que dar vuelta la lista para que sea compatible con los modulos de scypy

        # Obtengo mi polinomio del denominador en base a los polos que se encuentran en el semi-plano izquierdo
        myDenominator = pol.polyfromroots(gaussFilterPoles)

        # Retorno el numerador que siempre es 1
        # Retorno la parte real de los coeficientes del denominador ya que por aproximacion de la libreria
        # hay parte imaginaria para ordenes mayores a 5 que son muy muy pequeños, los desprecio :(

        num = [1]

        # Doy vuelta para que este correcto el array con coeficientes del denominador
        den = myDenominator.real[::-1]

        # Reemplazo s por tau.s para obtener el tau que quiero en el group_delay
        for i in range(len(den)):
            den[i] = (den[i] * (tau) ** (len(den) - i - 1))

        # Obtengo retardo de grupo
        w, h = signal.freqs(num, den)


        # NUEVO

        #########################
        # Normalizo             #
        group_delay = -np.diff(np.unwrap(np.angle(h))) / np.diff(w)
        group_delay = group_delay / group_delay[0] * tau

        nMax = nMax - 1

    else:
        nMax = n + 2

        while idealN == False:

            myGaussSum = 0
            imNumber = sympy.I
            nMax = (nMax + 1)
            s = sympy. \
                symbols("s")
            w = sympy.symbols("w")

            for k in range(1, nMax):
                # Defino la Sumatoria del Denominador de una Gaussiana#

                myGaussSum += (((-1) ** k) / (math.factorial(k)) * (s) ** (2 * k))

            rawGaussFilter = 1 / (1 + myGaussSum)

            # Separo en denominador y numerador # #ESTO NO ES NECESARIO. Quedo legacy
            rawGaussFilterNum, rawGaussFilterDen = sympy.fraction(rawGaussFilter)

            # Transformo el polinomio obtenido en [coefMax,...,coefMin]

            rawGaussFilterDenInCoeff = sympy.Poly(rawGaussFilterDen, s).all_coeffs()

            # Esto es el poliniomio del denominador contemplando todos los polos

            poles = np.poly1d(rawGaussFilterDenInCoeff)

            gaussFilterPoles = []

            # Filtro las raices con parte real negativa

            for pole in roots(poles):
                if pole.real < 0:
                    gaussFilterPoles.append(pole)

            # Esta funcion me devuelve el polinomio en un array en el orden a+bx**1+c**2+...+d**n
            # Tengo que dar vuelta la lista para que sea compatible con los modulos de scypy

            # Obtengo mi polinomio del denominador en base a los polos que se encuentran en el semi-plano izquierdo
            myDenominator = pol.polyfromroots(gaussFilterPoles)

            # Retorno el numerador que siempre es 1
            # Retorno la parte real de los coeficientes del denominador ya que por aproximacion de la libreria
            # hay parte imaginaria para ordenes mayores a 5 que son muy muy pequeños, los desprecio :(

            num = [1]

            # Doy vuelta para que este correcto el array con coeficientes del denominador
            den = myDenominator.real[::-1]

            # Reemplazo s por tau.s para obtener el tau que quiero en el group_delay
            for i in range(len(den)):
                den[i] = (den[i] * (tau) ** (len(den) - i - 1))

            # Obtengo retardo de grupo
            w, h = signal.freqs(num, den,(logspace(log10(wrg/1000), log10(wrg*100), 10000)))

            # NUEVO

            #########################
            # Normalizo             #
            group_delay = -np.diff(np.unwrap(np.angle(h))) / np.diff(w)

            temp_gd = group_delay / group_delay[0]

            group_delay = group_delay / group_delay[0] * tau

            myIndex = [m for m, i in enumerate(w) if i > wrg][0]


            if temp_gd[myIndex] > (1 - tol):
                idealN = True
                nMax = nMax - 1





    return [1],den,[],gaussFilterPoles,group_delay,w[1:],nMax

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
    wrg = 400
    tol = 1
    tau = 1e-3

    num,den,myZeros,myPoles,gd,wd,n = gaussFilter(A_p,A_a,w_p,w_a,w_max,wrg,tol,tau)
    print (n)
    #num2, den2, myZeros2, myPoles2, gd2, wd2 = gaussFilter(A_p, A_a, w_p, w_a, w_max, wrg, tol, tau, 6)
    #num3, den3, myZeros3, myPoles3, gd3, wd3 = gaussFilter(A_p, A_a, w_p, w_a, w_max, wrg, tol, tau, 9)
    #print (myPoles)

    system = signal.TransferFunction (num,den)

    print (num,den)
    print (myZeros,myPoles)
    w,mag,phase = signal.bode(system)


    plt.figure()

    plt.semilogx(w, phase)

    plt.show()

    plt.figure()
    plt.semilogx (wd,gd,label="n=2")
    #plt.semilogx(2*pi*wd2, gd2,label="n=3")
    #plt.semilogx(2*pi*wd3, gd3,label="n=4")
    plt.legend()

    plt.show()