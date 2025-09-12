import numpy as np

# Generate some random data
data = np.random.rand(5, 4, 3)

# Get the indices of the maximum values along the first axis
max_indices = np.argmax(data, axis=0)

print(max_indices)
