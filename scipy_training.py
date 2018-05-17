from numpy import poly1d
from scipy.optimize import minimize
from scipy.interpolate import interp1d

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

p = poly1d([1, 2, -1]) # makes a polynomial equation, here ax^2 + bx + c
print(p)
print(2 * p)
print(p ** 2)
print(p.deriv())

def add(a, b):
    return a + b

vec_add = np.vectorize(add)
x = [1, 2, 3]
y = [7, 8, 9]
print(vec_add(x, y)) # [8, 10, 12]

print(scipy.integrate.quad(lambda x: -x +1 , 0, 1)) # function and boundaries

def rosen(x):
   """The Rosenbrock function"""
   return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print(res.x)

x1 = np.linspace(0, 10, 11, endpoint=True)
y1 = np.sin(x1 ** 2 / 3)
f = interp1d(x1, y1, kind="cubic")
x2 = np.linspace(0, 10, 100, endpoint=True)
plt.plot(x1, y1,'o', color='blue', label='data')
plt.plot(x2, f(x2), '--', color='red', label='cubic')
plt.legend(loc='best')
plt.show()



