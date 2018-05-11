import numpy as np
import matplotlib . pyplot as plt

txt = np.loadtxt('data.txt', unpack=True)
x = txt[0]
y1 = txt[1]
y2 = txt[2]
y3 = txt[3]

plt.plot(x, y1, 'o', color='blue', label='CO')
plt.plot(x, y2, 'o', color='orange', label='GE')
plt.plot(x, y3, 'o', color='red', label='EM')
# np.polyfit(x, y, deg, optional parameters)
#   x: x-coordinates of the M sample points (x[i], y[i])
#   y: y-coordinates of the sample points. Several data sets of sample points sharing the same x-coordinates can be
#      fitted at once by passing in a 2D-array that contains one dataset per column.
#   deg: Degree of the fitting polynomial
# returns Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y). Returns a vector of
# coefficients p that minimises the squared error.
x1 = np.polyfit(x, y1, 2,)
x2 = np.polyfit(x, y2, 2,)
x3 = np.polyfit(x, y3, 2,)
# np.polyval(p, x)
#   p: 1D array of polynomial coefficients
#   x: A number, an array of numbers, or an instance of poly1d, at which to evaluate p.
# returns p[0]*x**(N-1) + p[1]*x**(N-2) + ... + p[N-2]*x + p[N-1]
w1 = np.polyval(x1, x)
w2 = np.polyval(x2, x)
w3 = np.polyval(x3, x)
plt.plot(x, w1, '--')
plt.plot(x, w2, '--')
plt.plot(x, w3, '--')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.legend(loc='upper right')
plt.ylim((0, 180))
plt.show()

T = txt[1] + txt[2] + txt[3]
print(T)
plt.plot(x, T, 'o', color='blue', label='people')
x4 = np.polyfit(x, T, 2)
w4 = np.polyval(x4, x)
plt.plot(x, w4, '--')
plt.show()
