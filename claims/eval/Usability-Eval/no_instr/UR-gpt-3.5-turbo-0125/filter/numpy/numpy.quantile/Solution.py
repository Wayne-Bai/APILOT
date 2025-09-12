
import numpy as np

# Generate some random data for demonstration
data = np.random.rand(5, 5)

# Specify the axis and quantile value
axis = 1
q = 0.5

# Compute the q-th quantile of the data along the specified axis
quantile_value = np.percentile(data, q*100, axis=axis)

print("Quantile value along axis {}: {}".format(axis, quantile_value))
