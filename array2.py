import numpy as np
a = 2*(np.eye(3,4,k = 0))
b = np.eye(3,4,k = 1)
c = a + b
print(c)