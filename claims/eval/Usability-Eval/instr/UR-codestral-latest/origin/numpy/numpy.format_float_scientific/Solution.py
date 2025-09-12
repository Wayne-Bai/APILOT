import numpy as np

def format_scientific(num):
    return np.format_float_scientific(num, precision=2)

# Test the function
print(format_scientific(12345.6789))
