import numpy as np
import matplotlib . pyplot as plt
from sympy import *

def graphic(v1, g, t):
    y = v1 * t - 1/2 * g * t **2
    v = diff(y, t)  # speed (first derivative)
    a = diff(v, t)  # acceleration (second derivative)

    t1, t2 = solve(y, t)
    total = [y, t1, t2, v, a]
    return total

T = np.arange(0, 20, 1)
x = graphic(5, 9.81, T)
plt.plot(T, x[0], '--')


plt.legend(loc='upper right')
plt.ylim((x[1], x[2]))
plt.show()
