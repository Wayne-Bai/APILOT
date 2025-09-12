import numpy as np

def format_float_scientific(value):
    return "{:.6e}".format(value)

# Example usage
float_value = 12345.6789
formatted_value = format_float_scientific(float_value)
print(formatted_value)
