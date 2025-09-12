import numpy as np

def format_float_as_decimal_string(value):
    # Format the float as a decimal string
    return np.format_float_positional(value, trim='k', precision=6)

# Example usage
float_value = 12345.6789
formatted_string = format_float_as_decimal_string(float_value)
print(formatted_string)
