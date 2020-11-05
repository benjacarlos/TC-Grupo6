# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import legendre as legendre
from template import Type  as Type
from template import Approximation  as Approximation
from template import template

import cauer as cauer
import gauss as gauss

#dummy functions
def plot(template):
    if template.should_be_drawn():

        if template.type == Type.LPN:
            w, h = signal.freqs(template.normalized_num, template.normalized_den, worN=np.linspace(0, 1e2, 1000))
        else:
            w, h = signal.freqs(template.actual_num, template.actual_den, worN=np.linspace(1e4, 1e6, 1000))

        plt.semilogx(w, 20 * np.log10(abs(h)), label='n')

        plt.title('Elliptic filter frequency response (rp=5, rs=40)')
        plt.xlabel('Frequency [radians / second]')
        plt.ylabel('Amplitude [dB]')
        plt.margins(0, 0.1)
        plt.grid(which='both', axis='both')
        # plt.axvline(fc, color='green')  # cutoff frequency
        # plt.axvline(w_a, color='red')  # cutoff frequency
        # plt.axvline(w_p, color='red')  # cutoff frequency

        # plt.axhline(-A_a, color='green')  # rs
        # plt.axhline(-A_p, color='green')  # rp
        # plt.plot([0, fc], [-A_p, -A_p], color='green', alpha=0.8)
        plt.tight_layout()

        if template.should_draw_template():
            if template.type==Type.LP:
                rectangle_p = plt.Rectangle((0, -template.data["A_p"]), template.data["w_p"], -template.data["A_a"] - 100, fc='violet', alpha=0.8)
                rectangle_a = plt.Rectangle((template.data["w_a"], -template.data["A_a"]), 1e6 - template.data["w_p"], template.data["A_a"] + 30, fc='violet', alpha=0.8)

            if template.type==Type.LPN:
                rectangle_p = plt.Rectangle((0, -template.data["A_p"]), 1, -template.data["A_a"] - 100, fc='violet', alpha=0.8)
                rectangle_a = plt.Rectangle((template.w_a_n, -template.data["A_a"]), 1e6 - 1, template.data["A_a"]+30 , fc='violet', alpha=0.8)

            if template.type==Type.HP:
                rectangle_p = plt.Rectangle((0, 0), template.data["w_a"], -template.data["A_a"], fc='violet', alpha=0.8)
                rectangle_a = plt.Rectangle((template.data["w_p"], -template.data["A_p"]), 1e6 - template.data["w_p"], -template.data["A_a"] - 200, fc='violet', alpha=0.8)

            if template.type==Type.BP:
                rectangle_p = plt.Rectangle((0, -template.data["A_a"]), template.data["w_a_m"], template.data["A_a"], fc='violet', alpha=0.8)
                rectangle_p1 = plt.Rectangle((template.data["w_a"], -template.data["A_a"]), template.data["w_a"]+10e6, template.data["A_a"], fc='violet', alpha=0.8)
                rectangle_a = plt.Rectangle((template.data["w_p_m"], -template.data["A_p"]), template.bw, -template.data["A_a"] - 200, fc='violet', alpha=0.8)

                plt.gca().add_patch(rectangle_p1)

            if template.type==Type.BR:
                rectangle_p = plt.Rectangle((0, -template.data["A_p"]), template.data["w_p_m"], template.data["A_a"]-300, fc='violet', alpha=0.8)
                rectangle_p1 = plt.Rectangle((template.data["w_p"], -template.data["A_p"]), template.data["w_a"]+10e6, template.data["A_a"]-300, fc='violet', alpha=0.8)
                rectangle_a = plt.Rectangle((template.data["w_a_m"], 0), template.data["w_a"]-template.data["w_a_m"], -template.data["A_a"], fc='violet', alpha=0.8)

                plt.gca().add_patch(rectangle_p1)

            plt.gca().add_patch(rectangle_p)
            plt.gca().add_patch(rectangle_a)

        plt.show()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

#creo un diccionario para pasar los datos

    # data = {
    #     "A_a" : 30,
    #     "A_p" : 3,
    #     "w_a" : 120e3,
    #     "w_a_m" : 80e3,
    #     "w_p" : 150e3,
    #     "w_p_m" : 50e3
    # }
    # temp_legen=template(Type.BR,Approximation.Legendre,data)
    # plot(temp_legen)
    # data.clear()
    #
    # data = {
    #     "A_a": 30,
    #     "A_p": 3,
    #     "w_a": 120e3,
    #     "w_p": 80e3,
    # }
    # temp_legen_2 = template(Type.LP, Approximation.Legendre, data)
    # plot(temp_legen_2)
    # data.clear()

    # data = {
    #     "A_a" : 30,
    #     "A_p" : 3,
    #     "w_a" : 120e3,
    #     "w_a_m" : 80e3,
    #     "w_p" : 150e3,
    #     "w_p_m" : 50e3
    # }
    data = {
        "A_a" : 10,
        "A_p" : 3,
        "w_a" : 100e3,
        # "w_a_m" : 80e3,
        "w_p" : 200e3,
        # "w_p_m" : 20e3,
        "n" : 0,     #poner valor != 0 para harcodear
        "Q_max": 0, #poner valor != 0 para harcodear
        "d": 0 #coeficiente de desnormalización, por defecto 0
    }
    temp_legen_3 = template(Type.HP, Approximation.Legendre, data)
    temp_legen_3.type = Type.LPN
    plot(temp_legen_3)
    temp_legen_3.type = Type.HP
    plot(temp_legen_3)




