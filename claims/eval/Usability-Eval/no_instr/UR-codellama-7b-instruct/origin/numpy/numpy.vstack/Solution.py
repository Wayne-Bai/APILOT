import numpy as np

# Define two arrays to be stacked
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack the arrays vertically (row-wise)
c = np.vstack((a, b))
print(c)  # Output: [[1 2 3]
           #           [4 5 6]]
