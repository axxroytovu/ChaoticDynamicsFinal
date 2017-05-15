"""
Problem 7
Mandelbrot Set
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
#xmin, xmax, ymin, ymax = -1.3, -0.8, -0.6, -0.1
xmin, xmax, ymin, ymax = -1, -0.9, -0.35, -0.25

xx, yy = np.meshgrid(np.linspace(xmin, xmax, 2000), np.linspace(ymin, ymax, 2000))
complex = xx + yy*1.0j
complex0 = complex+0.0
show = np.zeros(complex.shape)+100

for i in tqdm(range(100)):
    showx = np.zeros(complex.shape)+100
    complex1 = complex**2 + complex0
    complex[show == 100] = complex1[show == 100]
    showx[np.abs(complex) > 10] = i
    show[show == 100] = showx[show == 100]
    complex[np.abs(complex) > 10] = 0
    
plt.imshow(show, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap="nipy_spectral_r", clim=[0,100])
plt.show()
    