import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 6, 7, 8])
c = np.concatenate((a, b))
print(np.unique(c))