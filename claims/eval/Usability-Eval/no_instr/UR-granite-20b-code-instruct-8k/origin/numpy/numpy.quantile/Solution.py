
import numpy as np

data = np.array([1, 2, 3, 4, 5])
q = 0.5
axis = 0

quantile = np.quantile(data, q, axis=axis)
print(quantile)
