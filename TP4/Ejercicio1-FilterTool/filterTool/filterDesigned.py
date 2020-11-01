from cauer import cauerFilter
from gauss import gaussFilter
from legendre import legendreFilter

class filterDesigned():
    def __init__(self,aA,aP,Fa,Fp,filterType,approximationType,orderNumber,maximumQ,denormalization):
        self.Aa = aA
        self.Ap = aP
        self.Fa = Fa
        self.Fp = Fp
        self.filterType = filterType
        self.approximationType = approximationType
        self.orderNumber = orderNumber
        self.maximumQ = maximumQ
        self.denormalization = denormalization

        print (self.approximationType)

        if self.approximationType == "Cauer":
            self.thisFilter = cauerFilter(self.Ap,self.Aa,self.Fp,self.Fa,1e6)
            self.label = "Cauer Approximation"

        elif self.approximationType == "Legendre":
            self.label = "Legendre Approximation"

        elif self.approximationType == "Gauss":
            self.label = "Gauss Approximation"




