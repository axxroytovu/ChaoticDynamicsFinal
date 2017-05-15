"""
Problem 3
Henon Map
"""

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def Henon(x, y, a=1.4, b=0.3):
    return y + 1 - a*x*x, b*x

x = [0.5]
y = [0]

for i in tqdm(xrange(1000000)):
    xn, yn = Henon(x[-1], y[-1])
    x.append(xn)
    y.append(yn)

plt.plot(x[::100], y[::100], 'k.', rasterized=True)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Henon Map')
plt.savefig('P3.png', format='png', dpi=300)