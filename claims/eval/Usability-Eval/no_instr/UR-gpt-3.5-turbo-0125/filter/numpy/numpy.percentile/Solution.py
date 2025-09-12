
import numpy as np

# Create a sample array
data = np.array([[10, 7, 4], [3, 2, 1]])

# Compute the q-th percentile along axis 1 (row-wise)
percentile_q = 50
result = np.percentile(data, q=percentile_q, axis=1)

print("The", percentile_q, "th percentile of the data along axis 1 is:", result)
