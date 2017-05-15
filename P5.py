"""
Problem 5
Cubic Map
"""

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def Cubic(X, r):
    return r*x - x*x*x


r = np.linspace(0,3,1000)
x0 = np.ones(1000) * 0.1
x = x0+0.
xl = []
for i in tqdm(xrange(10000)):
    x = Cubic(x, r)
    #plt.plot(r, x)
    #plt.show()
    if i > 9900:
        xl.append(x+0.)

for ri, xi in zip(r, zip(*xl)):
    plt.plot(ri*np.ones(99), xi, 'k.')
plt.grid()
plt.title('Fixed points of Cubic Map')
plt.xlabel('r')
plt.ylabel('Fixed points of x')
plt.savefig('P5.png', format='png', dpi=300)
