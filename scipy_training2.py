import numpy as np
from scipy import linalg

A = np.array([[5], [6]])
B = np.array([[4, 1], [2, 2]])
print(A.T)
print(A)
print(B)
print(linalg.inv(B)) #inverse
print(B * A)
print(B.dot(A)) # [5*4 + 6*1]
                # [5*2 + 6*2]
print(linalg.det(B))
print(linalg.inv(B).dot(A))
print(linalg.solve(B, A))   #Solve a linear matrix equation, or system of linear scalar equations.

a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
r = np.dot(a, b)
print(r)    # 4*1 + 1*0, 4*0 + 1*1, ...
print(a)
