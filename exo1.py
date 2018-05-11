import numpy as np


def vgsvds2id(k, VT0, Lam, VGs, VDs):

    Id1 = k * VDs * (VGs - VT0 - Lam/2*VDs)
    Id2 = k * 1/(2 * Lam) * (VGs-VT0) ** (1/2)
    I = (Id1, Id2)
    return I

# np.arange(a, b, x)
#   a: undervalue
#   b: uppervalue
#   range between each value
VGs = np.arange(1, 10, 0.1) # forms a line matrix
# x.reshape(a,b)
#   x: the array you want to reshape
#   a: number of lines
#   b: number of columns
VGs.reshape(1,90)
VDs = np.arange(1,10,.1)
# VDs.reshape(1, 90)


v = vgsvds2id(6e-3, 1, 1.15, VGs, VDs)
print(v)
