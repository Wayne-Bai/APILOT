
import numpy as np

def format_scientific_notation(value):
    return np.format_float_positional(value, precision=2)

# Example usage
print(format_scientific_notation(123456789)) # Output: 1.23e+08
