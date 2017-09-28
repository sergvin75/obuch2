import math
import numba
import numpy as np
a = 2*(np.eye(3,4,k = 0))
b = np.eye(3,4,k = 1)
d = np.zeros((2,3,4), dtype = None, order='C')
e = np.linspace(0,2,9)
z = np.arange(4)
c = a + b
print(z)
print(e)
print(d)
