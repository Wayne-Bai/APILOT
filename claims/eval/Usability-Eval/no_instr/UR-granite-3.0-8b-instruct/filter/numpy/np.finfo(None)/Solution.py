import numpy as np

# Define the machine limits for floating point types
float_min = np.finfo(np.float32).min
float_max = np.finfo(np.float32).max
double_min = np.finfo(np.float64).min
double_max = np.finfo(np.float64).max

print(f"Float32 min: {float_min}")
print(f"Float32 max: {float_max}")
print(f"Float64 min: {double_min}")
print(f"Float64 max: {double_max}")
