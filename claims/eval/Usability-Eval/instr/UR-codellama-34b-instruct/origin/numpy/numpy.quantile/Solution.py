
import numpy as np

# Example data
data = np.array([1, 2, 3, 4, 5])

# Compute the q-th quantile of the data along the axis 0
quantile = np.quantile(data, q=0.75, axis=0)
print("Quantile:", quantile)
