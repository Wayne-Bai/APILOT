# Import required libraries
import numpy as np

# Define a floating point number
num = 234.5678

# Format the number in scientific notation
num_sci = np.format_float_scientific(num, precision=2, unique=False)

# Print the formatted number
print(num_sci)
