import numpy as np

# Create a floating-point scalar
scalar = np.float32(3.141592653589793)

# Format the scalar as a decimal string in scientific notation
scientific_notation = np.format_float_scientific(scalar, precision=2)

print(scientific_notation)
