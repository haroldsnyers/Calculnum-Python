import numpy as np


def vgsvds2id(k, VT0, Lam, VGs, VDs):

    Id1 = k * VDs * (VGs - VT0 - Lam/2*VDs)
    Id2 = k * 1/(2 * Lam) * (VGs-VT0) ** (1/2)
    I = (Id1, Id2)
    return I


VGs = np.arange(1, 10, 0.1)
VGs.reshape(1,90)
VDs = np.arange(1,10,.1)


v = vgsvds2id(6e-3, 1, 1.15, VGs, VDs)
print(v)
