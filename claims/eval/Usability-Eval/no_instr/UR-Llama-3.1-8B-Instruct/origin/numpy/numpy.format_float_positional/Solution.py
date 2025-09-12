import numpy as np

def format_decimal(as_integer, decimal_places):
    """
    Format a floating-point scalar as a decimal string in positional notation.
    
    Parameters:
    as_integer (bool): Whether to format as an integer or not.
    decimal_places (int): Number of decimal places to round to.
    
    Returns:
    str: Formatted decimal string.
    """
    value = np.round(np.float64(123.456), decimal_places)
    if (as_integer):
        return "{:.0f}".format(value)
    else:
        return "{:.{}f}".format(value, decimal_places)

print(format_decimal(as_integer=False, decimal_places=4))
print(format_decimal(as_integer=True, decimal_places=0))
