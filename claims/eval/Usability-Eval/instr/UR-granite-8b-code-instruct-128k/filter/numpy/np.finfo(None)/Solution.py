
import numpy as np

# Define the machine limits for floating point types
machine_limits = {
    'float32': np.finfo(np.float32).max,
    'float64': np.finfo(np.float64).max,
    'float128': np.finfo(np.float128).max
}

# Print the machine limits
print(machine_limits)
