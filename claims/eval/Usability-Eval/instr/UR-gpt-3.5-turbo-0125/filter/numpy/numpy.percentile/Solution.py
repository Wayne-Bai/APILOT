
import numpy as np

# Generate sample data
data = np.random.rand(10, 5)

# Define the percentile(s) to compute
percentiles = [25, 50, 75]

# Compute the q-th percentile of the data along the specified axis
result = np.percentile(data, percentiles, axis=0)
print(result)
