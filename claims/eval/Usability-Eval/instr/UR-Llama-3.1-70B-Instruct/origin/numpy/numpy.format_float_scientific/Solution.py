import numpy as np

def format_float_scientific(float_num):
    return "{:e}".format(float_num)

# test the function
print(format_float_scientific(12345.6789)) 

# or directly with numpy
float_num = np.float64(12345.6789)
print(f"{float_num:e}")
