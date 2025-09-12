import numpy as np

# Create a floating point scalar
x = np.float64(3.141592653589793)

# Format the floating-point scalar as a decimal string in positional notation
x_str = "{:.15f}".format(x)

print(x_str)
