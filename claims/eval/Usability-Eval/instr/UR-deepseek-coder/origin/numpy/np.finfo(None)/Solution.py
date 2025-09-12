import numpy as np

# Machine limits for floating point types

# For float16
float16_epsilon = np.finfo(np.float16).eps
float16_min = np.finfo(np.float16).min
float16_max = np.finfo(np.float16).max

# For float32
float32_epsilon = np.finfo(np.float32).eps
float32_min = np.finfo(np.float32).min
float32_max = np.finfo(np.float32).max

# For float64
float64_epsilon = np.finfo(np.float64).eps
float64_min = np.finfo(np.float64).min
float64_max = np.finfo(np.float64).max

# For float128 (if available)
try:
    float128_epsilon = np.finfo(np.float128).eps
    float128_min = np.finfo(np.float128).min
    float128_max = np.finfo(np.float128).max
except ValueError:
    float128_epsilon = None
    float128_min = None
    float128_max = None

# Print the results
print(f"float16 epsilon: {float16_epsilon}")
print(f"float16 min: {float16_min}")
print(f"float16 max: {float16_max}")

print(f"float32 epsilon: {float32_epsilon}")
print(f"float32 min: {float32_min}")
print(f"float32 max: {float32_max}")

print(f"float64 epsilon: {float64_epsilon}")
print(f"float64 min: {float64_min}")
print(f"float64 max: {float64_max}")

if float128_epsilon is not None:
    print(f"float128 epsilon: {float128_epsilon}")
    print(f"float128 min: {float128_min}")
    print(f"float128 max: {float128_max}")
else:
    print("float128 is not available on this system.")
