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
    k=1/w_a
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
        # print(p)
        p = p[p.real < 0]

        #z = [element * cte_des for element in z]

        print(p)

        k = float(np.prod(np.abs(p)))

        z = []

        num,den = signal.zpk2tf(z,p,k)
        w, h = signal.freqs(num, den, worN=np.linspace(w_a, w_a, 1))
        current_att=20 * np.log10(abs(h))
        print(n)
        print(abs(current_att))

        if np.abs(current_att) >= A_a or n_hardcodeado != 0:
            break
        else:
            n += 1

    w, h = signal.freqs(num, den, worN=np.linspace(1, w_a, 1000))
    array = np.abs(np.asarray(20 * np.log10(abs(h))))
    idx = (np.abs(array - A_a)).argmin()
    w_a_prima=w[idx]
    A_a_detec=array[idx]

    den = den[::-1]
    w_a_prima=inversefunc(polynomial.Polynomial(den/k), 10**(-A_a/20))
    print(w_a_prima)
    if cte_des!=0:
        #w_a_prima=inversefunc(polynomial.Polynomial(den),A_a)
        print(w_a_prima)
        cte_desnormalizacion = 1 + ((1 / (k*w_a_prima)) - 1) * cte_des
        p = [element * cte_desnormalizacion for element in p]
        k = float(np.prod(np.abs(p)))
        num,den = signal.zpk2tf(z,p,k)

    return z, p, k, n

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

    #print(a)
    domain = [F(-1), F(1)]

    serie = legen.Legendre(a,domain)
    #print(serie)
    serie = serie.convert(domain, polynomial.Polynomial)

    if n % 2:  # impar n
        # sum(a_n * P_n(x))**2
        integrand = serie ** 2
    else:  # even N
        # (x + 1) * sum(a_n * P_n(x))**2
        integrand = P([F(1), F(1)]) * serie ** 2

    # Integrate (using fractions; indefint.integ() returns floats)
    indefint = P(polynomial.polynomial.polyint(integrand.coef), domain)

    # Evaluate integral from -1 to 2*omega**2 - 1
    defint = indefint(P([F(-1), F(0), F(2)])) - indefint(-1)
    #print(defint)
    # Fractions have been cancelled; outputs are all integers
    # Return in order of decreasing powers of omega
    #return defint
    return [int(round(x,0)) for x in defint.coef[::1]]

