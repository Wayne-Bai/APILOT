import numpy as np

def format_float_sci_notation(value):
    return np.format_float_scientific(value=value, precision=3)

# Example usage
float_value = 12345.6789
formatted_value = format_float_sci_notation(float_value)
print(formatted_value)
