"""
Problem 8
Avalanches
"""

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import itertools as itr

def CSand(Sand, CRITVAL):
    SandX = Sand[1:, :] - Sand[:-1, :]
    SandY = Sand[:, 1:] - Sand[:, :-1]
    MaxTotalX = np.unravel_index(np.argmax(np.abs(SandX)), SandX.shape)
    MaxTotalY = np.unravel_index(np.argmax(np.abs(SandY)), SandY.shape)
    if abs(SandX[MaxTotalX]) >= abs(SandY[MaxTotalY]):
        MaxTotCoord = MaxTotalX
        Dir = 0
    else:
        MaxTotCoord = MaxTotalY
        Dir = 1
    Value = [SandX, SandY][Dir][MaxTotCoord]
    PosNeg = np.sign(Value) == 1
    #print MaxTotCoord, Dir, PosNeg, Value
    #print Sand
    #raw_input()
    return abs(Value)>CRITVAL, [abs(Value),list(MaxTotCoord),Dir,PosNeg]

Asize = []
CritStatic = 7
CritDynamic = 6

for i in tqdm(xrange(10000)):
    Sand = np.zeros((10,10))
    check = True
    size = 0
    while True:
        i, j = np.random.randint(10, size=2)
        Sand[i, j] += 1
        Av, [V, C, D, P] = CSand(Sand, CritStatic)
        while Av:
            size += V/2
            #print V, C, D, P
            C[D] += P
            #print C
            P = P*2 - 1
            #print P
            Sand[C[0], C[1]] -= V/2
            #print Sand
            C[D] -= P
            #print C
            Sand[C[0], C[1]] += V/2
            #print Sand
            #raw_input()
            Av, [V, C, D, P] = CSand(Sand, CritDynamic)
            if not Av:
                break
        else:
            continue
        Asize.append(size)
        break
plt.hist(Asize)
plt.grid()
plt.xlabel('Avalanche Size')
plt.ylabel('Number of Occurences')
plt.title('Model of Avalanche Occurrence')
plt.savefig('P8.png', format='png', dpi=300)
