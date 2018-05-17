import numpy as np

x = np.array([[1, 2, 5], [3, 4, 5], [5, 6, 7]])
print(x)
print(x.shape)
print(x.ndim)
print(x[0][1])  # line 0 column 1
print(x[0])     # line 0
print(x[0, 1]) # line 0 column 1
print(x[:, 2])  # all the lines, column 2
print(x[2][:])  # line 2
y = np.array([[1, 2], [3, 4], [5, 6]])
print(y)
print(y.reshape((2,3)))
print(y.transpose())
print(y.flatten())   # makes a (1, x) array
z = y[[0, 2], :] # line 0 and 2, all the columns
print(z)
print(z.diagonal())
print(z.trace())
print(x.trace()) # sum of the diagonal values
print(z.sum(axis=1)) # sum of the values of each line (axis 1)
print(z.sum(axis=0)) # sum of the values of each column ( axis 0)