import numpy as np

# Define a floating-point scalar
scalar = 1.23456789e-10

# Format the scalar as a decimal string in scientific notation
formatted_scalar = np.format_float_scientific(scalar, precision=2)

print(formatted_scalar)
