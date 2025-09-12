import numpy as np

# Get the machine epsilon for float64
epsilon = np.finfo(np.float64).eps
print("Machine epsilon for float64:", epsilon)

# Get the machine epsilon for float32
epsilon = np.finfo(np.float32).eps
print("Machine epsilon for float32:", epsilon)

# Get the maximum and minimum values for float64
max_val = np.finfo(np.float64).max
min_val = np.finfo(np.float64).min
print("Maximum value for float64:", max_val)
print("Minimum value for float64:", min_val)

# Get the maximum and minimum values for float32
max_val = np.finfo(np.float32).max
min_val = np.finfo(np.float32).min
print("Maximum value for float32:", max_val)
print("Minimum value for float32:", min_val)
