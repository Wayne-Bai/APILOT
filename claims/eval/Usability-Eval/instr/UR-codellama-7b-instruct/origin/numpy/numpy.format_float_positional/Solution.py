
import numpy as np

def format_float_positional(number, precision=None):
    """Format a floating-point scalar as a decimal string in positional notation.
    
    Parameters:
        number (float): The floating-point value to be formatted.
        precision (int, optional): The maximum number of significant digits to include in the result. Defaults to 6 if not provided.
    
    Returns:
        str: The formatted string representation of the floating-point scalar in positional notation.
    """
    if precision is None:
        precision = 6
    return np.format_float_positional(number, precision)
