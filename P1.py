"""
Problem 1
Lorenz Attractors at different R values
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from tqdm import tqdm


def Lorenz(X, r=1., sigma=10., b=8./3.):
    Xdot = sigma*(X[1]-X[0])
    Ydot = r*X[0] - X[1] - X[0]*X[2]
    Zdot = X[0]*X[1] - b*X[2]
    return np.array([Xdot, Ydot, Zdot])


x0 = [3., 0., 0.]
r = 100
alpha = 0.01

for i, r in tqdm(enumerate([10, 22, 24.5, 100, 126.52, 400])):
    x = np.array(x0)

    XL = [x+0]

    for j in tqdm(xrange(10000)):
        k1 = Lorenz(x, r)
        k2 = Lorenz(x + k1*alpha/2., r)
        k3 = Lorenz(x + k2*alpha/2., r)
        k4 = Lorenz(x + k3*alpha, r)
        x += alpha*(k1 + 2*k2 + 2*k3 + k4)/6
        XL.append(x+0)

    XX, YY, ZZ = zip(*XL)


    plt.plot(XX, YY)
    plt.grid()
    plt.title('Lorenz Attractor with r = {}'.format(r))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('P1{}.png'.format(i), format='png', dpi=300)
    plt.close()
    
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(XX, YY, ZZ)
    plt.grid()
    plt.title('Lorenz Attractor with r = {}'.format(r))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.zlabel('z')
    plt.show()
    '''
