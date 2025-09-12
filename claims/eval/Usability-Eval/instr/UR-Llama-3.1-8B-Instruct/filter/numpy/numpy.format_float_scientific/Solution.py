import numpy as np

# Define a floating-point scalar
num = 123456.789

# Format the number as a decimal string in scientific notation
formatted_num = np.format_float_scientific(num, precision=6, unique=False)

print(formatted_num)
