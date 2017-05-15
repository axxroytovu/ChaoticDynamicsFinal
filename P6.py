"""
Final - Problem 6
2 versions, top version is vectorized, bottom version is not
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#Favorite Functions:

def Standard(Cpx):
    return Cpx**3
    
def Offset(Cpx):
    return Cpx**3 + 0.43
    
def Squared(Cpx):
    return Cpx**2 + 0.25 + 0.55j


def Vectorized(Function, xmin, xmax, ymin, ymax):
    xr = np.linspace(xmin, ymax, 2000)
    yr = np.linspace(xmin, ymax, 2000)

    XX, YY = np.meshgrid(xr, yr)
    Complex0 = XX + YY*1.j
    #plt.imshow(np.imag(Complex0))
    #plt.show()
    Complex = Complex0 + 0.
    Complex[np.abs(np.real(Complex)) > 10] = 10.
    Complex[np.abs(np.imag(Complex)) > 10] = 10.j
    show = np.zeros(Complex.shape)

    for i in tqdm(xrange(100)):
        showx = np.zeros(Complex.shape)
        Complex1 = Function(Complex)
        Complex[show == 0] = Complex1[show == 0]
        #plt.imshow(show)
        #plt.show()
        showx[np.abs(Complex) > 10] = 1
        showx[np.logical_or(np.abs(np.real(Complex)) < 10, np.abs(np.imag(Complex)) < 10)] *= -1
        Complex[np.abs(Complex) > 10] = 0
        show[show == 0] = showx[show == 0]
    plt.imshow(show, cmap="Greys_r", clim=[0, 1], extent=[xmin, xmax, ymin, ymax], origin='lower')
    plt.savefig('P6.png', format='png', dpi=300)
    
def NonVector(Function, min, max):
    xr = np.linspace(min, max, 2000)
    yr = np.linspace(min, max, 2000)

    XX, YY = np.meshgrid(xr, yr)
    Complex0 = XX + YY*1.j
    #plt.imshow(np.imag(Complex0))
    #plt.show()
    Complex = Complex0 + 0.
    Complex[np.abs(np.real(Complex)) > 10] = 10.
    Complex[np.abs(np.imag(Complex)) > 10] = 10.j
    show = np.zeros(Complex.shape)

    for row, zr in tqdm(list(enumerate(Complex))):
        for col, z in enumerate(zr):
            ziter = z+0.
            for i in xrange(100):
                ziter = Function(ziter)
                if np.abs(ziter) > 10:
                    break
            if abs(np.real(ziter)) < 10 or abs(np.imag(ziter)) < 10:
                show[row, col] = 1
    plt.imshow(show, cmap="Greys", clim=[0,1], extent=[min, max, min, max], origin='lower')
    plt.show()

for FN in [Offset]:
    Vectorized(FN, -2, 2, -2, 2)
