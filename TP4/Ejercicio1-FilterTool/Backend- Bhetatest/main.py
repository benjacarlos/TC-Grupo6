# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import legendre as legendre
import cauer as cauer
import gauss as gauss

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A_a=70
    A_p=5
    w_p=100e3
    w_a=150e3
    w_max=1e6
    #cauer.cauer(A_p,A_a,w_p,w_a,w_max)
    legendre.legendre(A_p,A_a,w_p,w_a)


    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
