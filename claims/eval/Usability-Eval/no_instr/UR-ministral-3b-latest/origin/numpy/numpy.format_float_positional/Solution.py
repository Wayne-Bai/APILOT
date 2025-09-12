import numpy as np

# Function to format a float as a decimal string
def format_float_as_decimal_string(num):
    return np.format_float_positional(num)

# Example usage
float_num = 1.1234567896
decimal_string = format_float_as_decimal_string(float_num)
print(f"'{decimal_string}' is the decimal string representation of {float_num}")
