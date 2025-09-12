import numpy as np

def format_float_as_decimal(scalar):
    formatted_string = "{0:.2f}".format(scalar)
    return formatted_string

# Test the function
scalar_value = 3.141592653589793
formatted_value = format_float_as_decimal(scalar_value)
print(formatted_value)
