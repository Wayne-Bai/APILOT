import numpy as np

# Define the data and the axis along which to compute the quantile
data = np.array([1, 2, 3, 4, 5])
axis = 0

# Compute the q-th quantile of the data along the specified axis
quantile = np.quantile(data, q=0.5, axis=axis)

print(quantile)
