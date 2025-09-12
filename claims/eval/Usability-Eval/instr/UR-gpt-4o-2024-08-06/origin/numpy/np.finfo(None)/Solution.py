import numpy as np

# Machine limits for floating point types
float32_info = np.finfo(np.float32)
float64_info = np.finfo(np.float64)

# Display the information for float32
print("float32:")
print(f"  Min: {float32_info.min}")
print(f"  Max: {float32_info.max}")
print(f"  Epsilon: {float32_info.eps}")
print(f"  Precision: {float32_info.precision}")

# Display the information for float64
print("float64:")
print(f"  Min: {float64_info.min}")
print(f"  Max: {float64_info.max}")
print(f"  Epsilon: {float64_info.eps}")
print(f"  Precision: {float64_info.precision}")
