import numpy as np

# Create a floating-point scalar
scalar = np.float64(42.123456789)

# Format the scalar as a decimal string in scientific notation
formatted_scalar = "{:e}".format(scalar)

print(formatted_scalar)
