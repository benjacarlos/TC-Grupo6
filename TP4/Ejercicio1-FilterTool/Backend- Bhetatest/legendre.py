from scipy import signal
import numpy as np
from numpy import polynomial
from scipy import signal
import matplotlib.pyplot as plt
from scipy.special import legendre as legendre_
import numpy.polynomial.legendre as legen
from fractions import Fraction as F
from numpy.polynomial import Polynomial as P
from numpy.polynomial.polynomial import polyval
from pynverse import inversefunc
import numpy.polynomial as polynomial



def legendre (A_p,A_a,w_p,w_a,n_hardcodeado,cte_des):

    epsilon=np.sqrt(10.0**(A_p/10)-1)
    print(epsilon)
    b=np.log10((10.0**(A_a/10)-1)/epsilon**2)

    plt.figure()



    if n_hardcodeado != 0:
        n=n_hardcodeado
    else:
        n = 1
    #Chequeo n mínimo
    while True:
        serie = get_equation(n)
        iter = 0
        print(n)
        print(serie)
        # s=jw  ->  -s^2=w^2
        for x in serie:
            if iter % 2 == 0:
                if iter % 4 != 0:
                    serie[iter] = -x
            iter += 1
        serie = [element * epsilon for element in serie]
        serie[0] = 1

        serie.reverse()
        print(serie)

        p = np.roots(serie)
        # Me quedo con los polos de H(s)
        p = p[p.real < 0]

        print(p)

        gain = float(np.prod(np.abs(p)))

        z = []

        num,den = signal.zpk2tf(z,p,gain)
        w, h = signal.freqs(num, den, worN=np.linspace(w_a, w_a, 1))
        current_att=20 * np.log10(abs(h))
        print(n)
        print(abs(current_att))

        #Itero para ver si cumplo plantilla
        if np.abs(current_att) >= A_a or n_hardcodeado != 0:
            break
        else:
            n += 1

    #Proceso de desnormalizacion
    if cte_des != 0:  #Busco la frecuencia a la cual estoy en Aa con una estimación
        k = 1 / w_a
        w, h = signal.freqs(num, den, worN=np.linspace(1, w_a, 1000))
        array = np.abs(np.asarray(20 * np.log10(abs(h))))
        idx = (np.abs(array - A_a)).argmin()
        w_a_prima=w[idx]
        A_a_detec=array[idx]
        print(w_a_prima)

        #Calculo la constante de desnormalizacion
        cte_desnormalizacion = 1 + ((1 / (k*w_a_prima)) - 1) * cte_des
        #Multiplico los polos y la ganacia por la cte
        p = [element * cte_desnormalizacion for element in p]
        gain = float(np.prod(np.abs(p)))


    return z, p, gain, n

#Funcion para obtener el polinomio de legrende asociado
def get_equation(n):

    if (n % 2 == 1):
        k = (n - 1) / 2 #impar
    else:
        k = (n - 2) / 2 #par

    a = []

    # n impar
    if (n % 2 == 1):
        a0 = 1 / (np.sqrt(2) * (k + 1))
        a.append(a0)
        for i in range(int(k)):
            a.append((2 * (i+1) + 1) * a0)
    # n par
    else:
        # k par
        if (k % 2 == 0):
            a0 = 1 / np.sqrt((k + 1) * (k + 2))
            a.append(a0)
            for i in range(int(k)):
                # i par
                if ((i+1) % 2 == 0):
                    a.append((2 * (i+1) + 1) * a0)
                # i impar
                else:
                    a.append(0)
        # k impar
        else:
            a.append(0)
            if k > 0:
                a.append(3 / np.sqrt((k + 1) * (k + 2)))
                if k>1:
                    for i in range(int(k-1)):
                        # i impar
                        if ((i+2) % 2 == 1):
                            a.append(((2 * (i+2) + 1)/3) * a[1])
                        # i par
                        else:
                            a.append(0)

    domain = [F(-1), F(1)]

    serie = legen.Legendre(a,domain)
    serie = serie.convert(domain, polynomial.Polynomial)

    if n % 2:  # impar n
        integrand = serie ** 2
    else:
        integrand = P([F(1), F(1)]) * serie ** 2

    indefint = P(polynomial.polynomial.polyint(integrand.coef), domain)
    defint = indefint(P([F(-1), F(0), F(2)])) - indefint(-1)
    #print(defint)

    return [int(round(x,0)) for x in defint.coef[::1]]

