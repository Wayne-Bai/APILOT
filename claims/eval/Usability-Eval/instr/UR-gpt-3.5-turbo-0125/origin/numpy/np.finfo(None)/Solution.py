
import numpy as np

# Machine limits for floating point types
float32_min = np.finfo(np.float32).min
float32_max = np.finfo(np.float32).max
float64_min = np.finfo(np.float64).min
float64_max = np.finfo(np.float64).max

print("Machine limits for float32 type:")
print("Minimum value:", float32_min)
print("Maximum value:", float32_max)

print("\nMachine limits for float64 type:")
print("Minimum value:", float64_min)
print("Maximum value:", float64_max)
