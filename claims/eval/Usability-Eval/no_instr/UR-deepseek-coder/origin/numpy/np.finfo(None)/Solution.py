import numpy as np

# Machine limits for floating point types

# For float16
float16_eps = np.finfo(np.float16).eps
float16_min = np.finfo(np.float16).min
float16_max = np.finfo(np.float16).max
float16_tiny = np.finfo(np.float16).tiny
float16_resolution = np.finfo(np.float16).resolution

# For float32
float32_eps = np.finfo(np.float32).eps
float32_min = np.finfo(np.float32).min
float32_max = np.finfo(np.float32).max
float32_tiny = np.finfo(np.float32).tiny
float32_resolution = np.finfo(np.float32).resolution

# For float64 (also known as double precision)
float64_eps = np.finfo(np.float64).eps
float64_min = np.finfo(np.float64).min
float64_max = np.finfo(np.float64).max
float64_tiny = np.finfo(np.float64).tiny
float64_resolution = np.finfo(np.float64).resolution

# For float128 (if available)
try:
    float128_eps = np.finfo(np.float128).eps
    float128_min = np.finfo(np.float128).min
    float128_max = np.finfo(np.float128).max
    float128_tiny = np.finfo(np.float128).tiny
    float128_resolution = np.finfo(np.float128).resolution
except ValueError:
    float128_eps = None
    float128_min = None
    float128_max = None
    float128_tiny = None
    float128_resolution = None

# Print the results
print("Machine limits for float16:")
print(f"  Epsilon: {float16_eps}")
print(f"  Min: {float16_min}")
print(f"  Max: {float16_max}")
print(f"  Tiny: {float16_tiny}")
print(f"  Resolution: {float16_resolution}")

print("\nMachine limits for float32:")
print(f"  Epsilon: {float32_eps}")
print(f"  Min: {float32_min}")
print(f"  Max: {float32_max}")
print(f"  Tiny: {float32_tiny}")
print(f"  Resolution: {float32_resolution}")

print("\nMachine limits for float64:")
print(f"  Epsilon: {float64_eps}")
print(f"  Min: {float64_min}")
print(f"  Max: {float64_max}")
print(f"  Tiny: {float64_tiny}")
print(f"  Resolution: {float64_resolution}")

if float128_eps is not None:
    print("\nMachine limits for float128:")
    print(f"  Epsilon: {float128_eps}")
    print(f"  Min: {float128_min}")
    print(f"  Max: {float128_max}")
    print(f"  Tiny: {float128_tiny}")
    print(f"  Resolution: {float128_resolution}")
else:
    print("\nfloat128 is not available on this system.")
