import numpy as np

# Example floating-point scalar
number = 12345.6789

# Format the number in scientific notation
formatted_number = np.format_float_scientific(number, precision=3, exp_digits=2)

print(formatted_number)
