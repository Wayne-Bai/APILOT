import numpy as np

def format_scientific(float_scalar):
    return np.format_float_scientific(float_scalar, precision=3)

# example usage
float_scalar = 3.141592653589793
print(format_scientific(float_scalar))
