import numpy as np

def format_float_to_string(value):
    if isinstance(value, float):
        # Format the floating-point scalar in positional notation
        formatted_string = "{:.6f}".format(value)
        return formatted_string
    else:
        raise ValueError("The value provided is not a floating-point scalar.")

# Example usage
float_value = 12345.6789
formatted_string = format_float_to_string(float_value)
print(formatted_string)
