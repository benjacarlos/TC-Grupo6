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


def legendre (A_p,A_a,w_p,w_a,w_max):

    w_aN=w_a/w_p
    epsilon=np.sqrt(10.0**(A_p/10)-1)
    b=np.log10((10.0**(A_a/10)-1)/epsilon**2)
    plt.figure()
    #1ok    2ok

    for n in range(1,7,1):
    #    n = 5
        serie=get_equation(n)
        print(n)
        print(serie)
        iter=0
        #p = np.roots([-3, 0, -3, 0, -1, 0, 1])




        #s=jw  ->  -s^2=w^2
        for x in serie:
            if iter%2==0:
                if iter%4!=0:
                    serie[iter]=-x
            iter += 1

        serie[0]=1

        serie.reverse()
        print(serie)

        p=np.roots(serie)
        #print(p)
        p = p[p.real < 0]
        print(p)

        k = float(np.prod(np.abs(p)))

        z=[]
        #num, den = signal.zpk2tf(z, p, k)
        #print(den)

        #num_,dem_=signal.lp2lp(num,den,w_p)

        #print(dem_)


        # w, h = signal.freqs(num_, dem_, worN=np.linspace(1e4, w_max, 1000))
        #
        #
        # plt.semilogx(w, 20 * np.log10(abs(h)),label='n'+str(n))




        a=polyval(w_aN**2,serie)
        #print(a)
        #print(b)
        #print(serie)
        #print(p)

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
    # plt.tight_layout()
    # rectangle_p = plt.Rectangle((0, -A_p), w_p, -A_a-100, fc='violet', alpha=0.8)
    # rectangle_a = plt.Rectangle((w_a, -A_a), w_max-w_p, A_a+30, fc='violet', alpha=0.8)
    #
    # plt.gca().add_patch(rectangle_p)
    # plt.gca().add_patch(rectangle_a)
    # plt.show()

    return z, p, k

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
                    for i in range(int(k)):
                        # i impar
                        if ((i+2) % 2 == 1):
                            a.append((2 * (i+2) + 1) * a[1])
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

