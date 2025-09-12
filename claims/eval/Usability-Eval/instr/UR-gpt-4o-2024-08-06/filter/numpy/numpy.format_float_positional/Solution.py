import numpy as np

def format_float_positional(value, precision=8):
    """
    Format a floating-point scalar as a decimal string in positional notation.
    
    :param value: The floating-point scalar to format.
    :param precision: The number of decimal places to include.
    :return: A string representing the number in positional notation.
    """
    # Using numpy's formatting with `np.format_float_scientific` to achieve the positional formatting.
    formatted_value = f"{value:.{precision}f}"
    return formatted_value

# Example Usage
value = 0.000123456789
formatted_value = format_float_positional(value, precision=8)
print(formatted_value)
