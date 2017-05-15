import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy.optimize import curve_fit


def Lorenz(X, r=1., sigma=10., b=8./3.):
    Xdot = sigma*(X[1]-X[0])
    Ydot = r*X[0] - X[1] - X[0]*X[2]
    Zdot = X[0]*X[1] - b*X[2]
    return np.array([Xdot, Ydot, Zdot])
    
def LLFit(x, m, b):
    return np.exp(np.log(x)*m + b)

x0 = [3., 0., 0.]
r = 100
alpha = 0.01

x = np.array(x0)

XL = []

for j in tqdm(xrange(50000)):
    k1 = Lorenz(x, r)
    k2 = Lorenz(x + k1*alpha/2., r)
    k3 = Lorenz(x + k2*alpha/2., r)
    k4 = Lorenz(x + k3*alpha, r)
    x += alpha*(k1 + 2*k2 + 2*k3 + k4)/6
    if j > 10000:
        XL.append(x+0)

XX, YY, ZZ = zip(*XL)
#plt.plot(XX, YY, 'b.')
#plt.close()

cts = []
Count = 0
rs = np.logspace(-3,1,10)
for r in tqdm(rs):
    for i in tqdm(xrange(100)):
        cx, cy, cz = XL[np.random.choice(len(XL))]
        Count += sum([(x-cx)**2 + (y-cy)**2 + (z-cz)**2 < r**2 for x, y, z in XL])
    cts.append(Count/100)

CF, _ = curve_fit(LLFit, rs, cts)

plt.loglog(rs, cts, 'bx')
plt.loglog(rs, LLFit(rs, *CF), 'r--')
plt.show()