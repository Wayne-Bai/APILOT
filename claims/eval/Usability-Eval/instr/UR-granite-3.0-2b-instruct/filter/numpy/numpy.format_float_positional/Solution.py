import numpy as np

# Define a floating-point scalar
scalar = 123.456789

# Format the scalar as a decimal string in positional notation
formatted_scalar = np.format_float_fixed(scalar, decimal_places=5)

# Print the formatted scalar
print(formatted_scalar)
