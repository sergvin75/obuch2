import numpy as np

X = np.array([[1, 60], [1, 50], [1, 75]])
print(X)
Y = np.array([[10], [7], [12]])
print(Y)

Z = X.T
print(Z)
step1 = X.T.dot(X)
print(step1)
"""тут правиьно"""
step2 = np.linalg.inv(step1)
print(step2)
step3 = step2.dot(X.T)
print(step3)
b = step3.dot(Y)
print(b)
