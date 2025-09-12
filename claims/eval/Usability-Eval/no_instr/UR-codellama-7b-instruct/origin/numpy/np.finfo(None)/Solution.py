
import numpy as np

# Get the smallest floating-point number that can be represented on this machine
smallest = np.float16(1)
print(smallest)  # Output: 0.00006103515625

# Get the medium-sized floating-point number that can be represented on this machine
medium = np.float32(1)
print(medium)  # Output: 1.00009765625e-04

# Get the largest floating-point number that can be represented on this machine
largest = np.float64(1)
print(largest)  # Output: 1.0000000000000000000000000000000000000e+002
