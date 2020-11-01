from scipy import signal
import numpy as np

def legendre (A_p,A_a,w_p,w_a):

    k=w_p/w_a
    epsilon=np.sqrt(10.0**(A_p/10)-1)
    fact=np.log10((10.0**(A_a/10)-1)/epsilon**2)


    n=1
    if(n%2==1):
        k=(n-1)/2
    else:
        k=(n-2)/2
    a=[]

    #n impar
    if(n%2==1):
        a0=1/(np.sqrt(2)*(k+1))
        a.append(a0)
        for i in range(int(k)):
            a.append((2*i+1)*a0)
    #n par
    else:
        #k impar
        if (k % 2 == 1):
            a0=1/np.sqrt((k+1)(k+2))
            a.append(a0)
            for i in range(k):
                #i par
                if(i%2==0):
                    a.append((2 * i + 1) * a0)
                #i impar
                else:
                    a.append(0)
        #k par
        else:
            a.append(0)
            a.append(3 / np.sqrt((k + 1)(k + 2)))

            for i in range(k):
                #i par
                if(i%2==1):
                    a.append((2 * i + 1) * a[1])
                #i par
                else:
                    a.append(0)

    print(a)