import numpy as np

# Getting machine limits for floating point types
float32_info = np.finfo(np.float32)
float64_info = np.finfo(np.float64)

# Displaying the information
print("Float32 limits:")
print(f"  Minimum: {float32_info.min}")
print(f"  Maximum: {float32_info.max}")
print(f"  Smallest positive: {float32_info.eps}")

print("\nFloat64 limits:")
print(f"  Minimum: {float64_info.min}")
print(f"  Maximum: {float64_info.max}")
print(f"  Smallest positive: {float64_info.eps}")
