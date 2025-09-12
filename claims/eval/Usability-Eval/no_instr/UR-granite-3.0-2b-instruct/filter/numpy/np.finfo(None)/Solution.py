import numpy as np

# Set the machine limit for floating point types
np.seterr(all='raise')

# Example usage
try:
    x = np.finfo(np.float32).max
    print(f"Maximum value for float32: {x}")
except np.FInfoError:
    print("Maximum value for float32 exceeded")

try:
    y = np.finfo(np.float64).max
    print(f"Maximum value for float64: {y}")
except np.FInfoError:
    print("Maximum value for float64 exceeded")
