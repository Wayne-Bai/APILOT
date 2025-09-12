import numpy as np

def format_scientific_notation(x):
    return np.format_float_scientific(x)

# Example usage:
number = 12345.678
formatted_number = format_scientific_notation(number)
print(formatted_number)
