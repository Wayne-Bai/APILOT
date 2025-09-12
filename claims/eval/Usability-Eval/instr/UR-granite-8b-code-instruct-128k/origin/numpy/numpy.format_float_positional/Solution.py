import numpy as np

def format_float_positional(x, precision=2):
    return f'{x:.{precision}f}'

# Example usage
number = 3.14159
formatted_string = format_float_positional(number, precision=4)
print(formatted_string)  # Output: 3.1416
