import numpy as np

# machine limits for floating point types
max_float32 = np.finfo(np.float32).max
min_float32 = np.finfo(np.float32).min

max_float64 = np.finfo(np.float64).max
min_float64 = np.finfo(np.float64).min

print(f"Maximum float32 value: {max_float32}")
print(f"Minimum float32 value: {min_float32}")
print(f"Maximum float64 value: {max_float64}")
print(f"Minimum float64 value: {min_float64}")
