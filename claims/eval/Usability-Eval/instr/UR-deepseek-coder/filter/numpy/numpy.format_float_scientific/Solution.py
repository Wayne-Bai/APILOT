import numpy as np

def format_float_scientific(x, precision=None):
    if precision is None:
        precision = 15  # Default precision
    
    # Convert the number to a string in scientific notation
    formatted_str = f"{x:.{precision}e}"
    
    return formatted_str

# Example usage:
number = 12345.6789
formatted_number = format_float_scientific(number, precision=3)
print(formatted_number)
