import numpy as np

# Display machine limits for float32 and float64 floating point types
float32_limits = np.finfo(np.float32)
float64_limits = np.finfo(np.float64)

print("Float32 limits:")
print(f"  Smallest positive number: {float32_limits.tiny}")
print(f"  Largest positive number: {float32_limits.max}")
print(f"  Machine epsilon: {float32_limits.eps}")

print("\nFloat64 limits:")
print(f"  Smallest positive number: {float64_limits.tiny}")
print(f"  Largest positive number: {float64_limits.max}")
print(f"  Machine epsilon: {float64_limits.eps}")
