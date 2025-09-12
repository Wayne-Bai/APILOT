import numpy as np

def format_float_scientific(value, precision=6):
    """
    Format a floating-point scalar as a decimal string in scientific notation.
    
    Parameters:
    - value: float, the number to format.
    - precision: int, optional, number of digits after the decimal point.

    Returns:
    - str: The formatted string in scientific notation.
    """
    # Use np.format_float_scientific to format with the specified precision
    formatted_value = "{:.{prec}e}".format(value, prec=precision)
    return formatted_value

# Example usage:
value = 123456.789
formatted_value = format_float_scientific(value, precision=6)
print("Formatted in scientific notation:", formatted_value)
