
import numpy as np

# Define a float64 data type
float_dtype = np.float64

# Define the largest positive and negative values that can be represented by the float64 data type
largest_positive = np.finfo(float_dtype).max
largest_negative = -np.finfo(float_dtype).max

# Define a small positive and negative value to use as a reference
small_positive = 1e-20
small_negative = -1e-20

# Compute the machine limits for floating-point types using the largest positive and negative values
machine_limits = np.array([largest_positive, smallest_positive, largest_negative, smallest_negative])

print(machine_limits)
