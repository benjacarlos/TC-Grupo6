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
            rectangle_p = plt.Rectangle((0, -template.A_p), template.w_p, -template.A_a - 100, fc='violet', alpha=0.8)
            rectangle_a = plt.Rectangle((template.w_a, -template.A_a), 1e6 - template.w_p, template.A_a + 30, fc='violet', alpha=0.8)

            plt.gca().add_patch(rectangle_p)
            plt.gca().add_patch(rectangle_a)

        plt.show()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A_a=30
    A_p=3
    w_p=100e3
    w_a=150e3
    w_max=1e6
    #cauer.cauer(A_p,A_a,w_p,w_a,w_max)
    temp_legen=template(Type.LP,Approximation.Legendre,A_p,A_a,w_p,w_a,w_max)
    plot(temp_legen)
    #legendre.legendre(A_p,A_a,w_p,w_a,w_max)

