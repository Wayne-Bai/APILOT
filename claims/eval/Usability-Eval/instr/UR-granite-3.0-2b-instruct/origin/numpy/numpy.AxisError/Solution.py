import numpy as np

# Create a 1D numpy array
arr = np.array([1, 2, 3, 4, 5])

# Attempt to access an invalid axis (e.g., 5)
try:
    print(arr[:, 5])
except IndexError as e:
    print("IndexError:", e)

try:
    print(arr[np.axis[5]])
except ValueError as e:
    print("ValueError:", e)
