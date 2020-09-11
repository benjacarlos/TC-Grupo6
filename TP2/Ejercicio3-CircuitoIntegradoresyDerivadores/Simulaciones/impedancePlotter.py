import cmath, math, numpy
import math
import matplotlib.pyplot as plt

######################################################
# Definicion de elementos                            #
######################################################

R=5270
c=18.8e-9
avol=316227.76
pi=3.14159
wb=298.011

def myImpedanceCalculatorIntegrator(fStart,fEnd):
    myrange = numpy.linspace(fStart, fEnd, 3000000)
    impedances = []
    for f in myrange:
        Impedance = complex (R,-1/(2*pi*f*c*(1+avol/(1+(2*pi*f)/wb))))
        impedances.append(Impedance)

    magnitudes = []
    for magnitude in impedances:
        magnitudes.append (abs(magnitude))

    phases = []
    for phase in impedances:
        phases.append (numpy.degrees (cmath.phase(phase)))

    return myrange,magnitudes,phases

def myImpedanceCalculatorDerivator(fStart,fEnd):
    myrange = numpy.linspace(fStart, fEnd, 3000000)
    impedances = []
    for f in myrange:
        # Impedance = complex (R/(1+avol),1/(2*pi*f*c))
        Impedance = complex (0,-1/(2*pi*f*c))
        impedances.append(Impedance)

    magnitudes = []
    for magnitude in impedances:
        magnitudes.append (abs(magnitude))

    phases = []
    for phase in impedances:
        phases.append (numpy.degrees (cmath.phase(phase)))
    return myrange,magnitudes,phases

def plotInLog (frange,logPlot,myLabel):

    plt.semilogx(frange, logPlot,label=myLabel)
    plt.xscale('log')
    plt.grid(True, which="both")
    plt.minorticks_on()



def readLT (fileName):
    ltSpiceTXT = open(fileName, "r")
    EachLine = ltSpiceTXT.readlines()
    myLTImpedance = dict()
    myLTImpedance['f']=[]
    myLTImpedance['magnitude'] = []
    myLTImpedance['phase'] = []
    for i in range(1, len(EachLine)):
        pnt = 0
        frequency = ""
        real = ""
        imaginary = ""
        while EachLine[i][pnt] != '\t':
            frequency += EachLine[i][pnt]
            pnt += 1
        while EachLine[i][pnt] == ' ':
            pnt += 1
        while EachLine[i][pnt] != ',':
            real += EachLine[i][pnt]
            pnt += 1
        pnt += 1
        while EachLine[i][pnt] != '\n':
            imaginary += EachLine[i][pnt]
            pnt += 1
        myComplexImpedance = complex (float (real),float(imaginary))
        myLTImpedance['f'].append(float(frequency))
        myLTImpedance['magnitude'].append(abs(myComplexImpedance))
        myLTImpedance['phase'].append(math.atan(myComplexImpedance.imag/myComplexImpedance.real)*pi/180)
    return (myLTImpedance)


if __name__ == '__main__':

    ######################################################
    # Definir cual es el path al archivo de LT Spice     #
    ######################################################

    mySpiceImpedance = readLT(r"C:\Users\Nicolas Mestanza\Desktop\Draft3.txt")

    ######################################################
    # Definir desde que a que frecuencia quiero graficar #
    ######################################################

    fStart = 1e-2
    fEnd = 10000
    myrange, myMagnitude, myPhase = myImpedanceCalculatorIntegrator(fStart, fEnd)

    ######################################################
    # Grafico Magnitudes                                 #
    ######################################################

    #plotInLog(myrange, myMagnitude,"Teórica")
    #plotInLog(mySpiceImpedance['f'],mySpiceImpedance['magnitude'],"Simulada")
    #plt.ylabel("|Zin|")

    ######################################################
    # Grafico Fases                                      #
    ######################################################

    plotInLog(myrange, myPhase, "Teórica")
    plotInLog(mySpiceImpedance['f'],mySpiceImpedance['phase'],"Simulada")
    plt.ylabel("Fase Zin")


    plt.xlabel("Frecuencia (Hz)")
    plt.title("Impedancia de Entrada")
    plt.legend()
    plt.show()



