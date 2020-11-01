class filterDesigned():
    def __init__(self,aA,aP,Fa,Fp,filterType,approximationType,orderNumber,maximumQ,denormalization):
        self.AaInputFilter = aA
        self.ApInputFilter = aP
        self.FaInputFilter = Fa
        self.FpInputFilter = Fp
        self.filterType = filterType
        self.approximationType = approximationType
        self.orderNumber = orderNumber
        self.maximumQ = maximumQ
        self.denormalization = denormalization