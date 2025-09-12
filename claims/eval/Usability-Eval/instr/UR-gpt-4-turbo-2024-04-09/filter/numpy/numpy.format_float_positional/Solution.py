import numpy as np

def format_float(value):
    formatted_value = np.format_float_positional(value)
    return formatted_value

# Example usage
number = 0.123456
print(format_float(number))
