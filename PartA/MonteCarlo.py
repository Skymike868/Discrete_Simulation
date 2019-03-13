from __future__ import division

import numpy as np

from Bushing import get_Triangular
from Shaft import get_Shaft


def interfer_Probab(runs, left, mode, right, m, s):
    C = 0
    for count in range(1, runs):
        x = get_Triangular(left, mode, right)
        y = get_Shaft(m, s)
        if x < y:
            C = C+1
    # print(C)
    return C/runs


print('The Interference Probability is:',
      interfer_Probab(10000, 0.003, 1, 0.003, 1, 0.002))
