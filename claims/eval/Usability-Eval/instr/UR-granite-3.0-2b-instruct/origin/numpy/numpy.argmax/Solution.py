import numpy as np

# Sample data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find the maximum value along each column (axis=1)
max_indices = np.argmax(data, axis=1)

print("Maximum values and their indices:")
for i, row in enumerate(data):
    print(f"Row {i+1}: {row[max_indices[i]]}")
