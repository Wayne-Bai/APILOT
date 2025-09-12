
import numpy as np

# Create a sample 2D numpy array
data = np.array([[True, True, True],
                 [True, False, True],
                 [False, False, False]])

# Test whether all array elements along axis=1 evaluate to True
result = np.all(data, axis=1)

print(result)
