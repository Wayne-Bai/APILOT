import numpy as np

data = np.array([1, 2, 3, 4, 5])
q = 0.5
quantile = np.quantile(data, q)

print(quantile)