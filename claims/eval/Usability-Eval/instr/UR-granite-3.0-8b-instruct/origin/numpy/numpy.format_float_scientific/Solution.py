import numpy as np

def format_float_scientific(num):
    return np.format_float_scientific(num, precision=6, exp_zeros='0', sign=True, stripe=True, unique=True, fee=0)

# Test the function
print(format_float_scientific(1.23456789))
