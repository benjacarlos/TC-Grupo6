import cmath, math, numpy
import matplotlib.pyplot as plt

######################################################
# Definicion de elementos                            #
######################################################

R=5100
c=20e-9
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
        Impedance = complex (R/(1+avol),-1/(2*pi*f*c))
        impedances.append(Impedance)

    magnitudes = []
    for magnitude in impedances:
        magnitudes.append (abs(magnitude))

    phases = []
    for phase in impedances:
        phases.append (numpy.degrees (cmath.phase(phase)))
    return myrange,magnitudes,phases

def plotInLog (xlabel,ylabel,theTitle, frange,logPlot,fig):

    ax = fig.add_subplot()
    ax.semilogx(frange, logPlot)
    ax.set_xscale('log')
    ax.grid(True, which="both")
    ax.minorticks_on()
    ax.set_title(theTitle)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    #plt.show()


def readLT (fileName):
    ltSpiceTXT = open(r"C:\Users\Nicolas Mestanza\Desktop\Draft3.txt", "r")
    EachLine = ltSpiceTXT.readlines()
    print (EachLine)
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
        myLTImpedance['phase'].append(numpy.degrees(cmath.phase(myComplexImpedance)))
    return (myLTImpedance)

if __name__ == '__main__':
    mySpiceImpedance = readLT ("Draft5")
    fig = plt.figure()
    ######################################################
    # Definir desde que a que frecuencia quiero graficar #
    ######################################################

    fStart = 1e-2
    fEnd = 10000

    ######################################################
    # Grafico                                            #
    ######################################################

    myrange, myMagnitude,myPhase = myImpedanceCalculatorIntegrator(fStart,fEnd)
    #myrange, myMagnitude,myPhase = myImpedanceCalculatorDerivator(fStart,fEnd)

    plotInLog ("Frecuencia (Hz)","|Zin|","Impedancia de Entrada",mySpiceImpedance['f'],mySpiceImpedance['magnitude'],fig)

    plotInLog ("Frecuencia (Hz)","|Zin|","Impedancia de Entrada",myrange,myMagnitude,fig)
    #plotInLog("Frecuencia (Hz)", "Fase Zin", "Impedancia de Entrada", myrange, myPhase)
    plt.show()





