import cmath, math, numpy
import matplotlib.pyplot as plt

######################################################
# Definicion de elementos                            #
######################################################

R=5270
c=18.8e-9
avol=316227.76
pi=3.14159

def myImpedanceCalculatorIntegrator(fStart,fEnd):
    myrange = numpy.linspace(fStart, fEnd, 3000000)
    impedances = []
    for f in myrange:
        Impedance = complex (R,-1/(2*pi*f*c*(1+avol)))
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

def plotInLog (xlabel,ylabel,theTitle, frange,logPlot):
    fig, ax = plt.subplots()
    ax.semilogx(frange, logPlot)
    ax.set_xscale('log')
    ax.grid(True, which="both")
    # ax.minorticks_on()

    locmaj = plt.ticker.LogLocator(base=10, numticks=12)
    ax.yaxis.set_major_locator(locmaj)

    locmin = plt.ticker.LogLocator(base=10.0, subs=(0.2, 0.4, 0.6, 0.8), numticks=12)
    ax.yaxis.set_minor_locator(locmin)
    ax.yaxis.set_minor_formatter(plt.ticker.NullFormatter())

    ax.set_title(theTitle)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

if __name__ == '__main__':

    ######################################################
    # Definir desde que a que frecuencia quiero graficar #
    ######################################################

    fStart = 1e-2
    fEnd = 1e9

    ######################################################
    # Grafico                                            #
    ######################################################

    # myrange, myMagnitude,myPhase = myImpedanceCalculatorIntegrator(fStart,fEnd)
    myrange, myMagnitude,myPhase = myImpedanceCalculatorDerivator(fStart,fEnd)
    plotInLog ("Frecuencia (Hz)","|Zin|","Impedancia de Entrada",myrange,myMagnitude)
    plotInLog("Frecuencia (Hz)", "Fase Zin", "Impedancia de Entrada", myrange, myPhase)




