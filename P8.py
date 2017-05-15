"""
Problem 8
Avalanches
"""

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import itertools as itr

Asize = []
CRITVAL = 7

for i in tqdm(xrange(10000)):
    Sand = np.zeros((10,10))
    check = True
    while True:
        i, j = np.random.randint(10, size=2)
        Sand[i, j] += 1
        if i != 0:
            xm = abs(Sand[i, j] - Sand[i-1, j])
            if xm > CRITVAL:
                check = False
        else:
            xm = 0
        if j != 0:
            ym = abs(Sand[i, j] - Sand[i, j-1])
            if ym > CRITVAL:
                check = False
        else:
            ym = 0
        if j != 9:
            yp = abs(Sand[i, j] - Sand[i, j+1])
            if yp > CRITVAL:
                check = False
        else:
            yp = 0
        if i != 9:
            xp = abs(Sand[i, j] - Sand[i+1, j])
            if xp > CRITVAL:
                check = False
        else:
            xp = 0
        size = 0
        while not check:
            mx = max([xm, xp, ym, yp])
            print mx, xm, xp, ym, yp
            raw_input()
            if mx == xm:
                Sand[i, j] -= int(mx)/2
                Sand[i-1, j] += int(mx)/2
                i -= 1
                size += int(mx)/2
            if mx == xp:
                Sand[i, j] -= int(mx)/2
                Sand[i+1, j] += int(mx)/2
                i += 1
                size += int(mx)/2
            if mx == yp:
                Sand[i, j] -= int(mx)/2
                Sand[i, j+1] += int(mx)/2
                j += 1
                size += int(mx)/2
            if mx == ym:
                Sand[i, j] -= int(mx)/2
                Sand[i, j-1] += int(mx)/2
                j -= 1
                size += int(mx)/2
            check = True
            print i, j
            raw_input()
            #for i, j in itr.product(xrange(10), xrange(10)):
            if i != 0:
                xm = (Sand[i, j] - Sand[i-1, j])
                if xm > CRITVAL:
                    check = False
            else:
                xm = 0
            if j != 0:
                ym = (Sand[i, j] - Sand[i, j-1])
                if ym > CRITVAL:
                    check = False
            else:
                ym = 0
            if j != 9:
                yp = (Sand[i, j] - Sand[i, j+1])
                if yp > CRITVAL:
                    check = False
            else:
                yp = 0
            if i != 9:
                xp = (Sand[i, j] - Sand[i+1, j])
                if xp > CRITVAL:
                    check = False
            else:
                xp = 0
        if size:
            Asize.append(size)
            break
plt.hist(Asize)
plt.show()
