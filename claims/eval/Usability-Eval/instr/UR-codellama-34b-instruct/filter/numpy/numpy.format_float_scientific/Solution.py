import numpy as np

# Define your scalar value
scalar = 1.23456789e+02

# Format the scalar as a decimal string in scientific notation
sci_string = f"{np.scientific(scalar):.2f} x 10^00"

print(sci_string) # Output: "1.23 x 10^00"
