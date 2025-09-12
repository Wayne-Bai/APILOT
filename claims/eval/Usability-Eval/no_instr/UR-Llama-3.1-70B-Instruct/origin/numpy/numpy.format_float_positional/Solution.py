import numpy as np

def float_to_decimal_string(num):
    """
    Format a floating-point scalar as a decimal string in positional notation.

    Args:
    num (float): The input floating-point number.

    Returns:
    str: A decimal string representation of the input number.
    """
    # Use the format function to convert the float into a string with decimal places
    decimal_string = "{0:f}".format(num)
    
    return decimal_string

# Example usage:
num = np.float64(1.23456789)  # Create a numpy float64 object
print(float_to_decimal_string(num))  # Output: 1.234568
