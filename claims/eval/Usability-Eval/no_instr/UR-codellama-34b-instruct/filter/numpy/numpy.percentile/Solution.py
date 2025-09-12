import numpy as np

# Generate some random data
data = np.random.randn(10, 5)

# Compute the 25th, 50th, and 75th percentiles along axis 0 (columns)
p25 = np.percentile(data, 25, axis=0)
p50 = np.percentile(data, 50, axis=0)
p75 = np.percentile(data, 75, axis=0)

# Print the results
print("25th percentile:", p25)
print("50th percentile:", p50)
print("75th percentile:", p75)
