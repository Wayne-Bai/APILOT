import numpy as np

# Function to format a floating-point scalar as a decimal string in scientific notation
def format_scientific(num):
    return f"{num:.2e}"

# Test the function
num = 123456.789
print(format_scientific(num))
