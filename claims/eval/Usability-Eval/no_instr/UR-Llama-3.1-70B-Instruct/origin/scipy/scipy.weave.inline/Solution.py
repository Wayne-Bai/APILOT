import scipy
from scipy import weave
import numpy as np

# Define a function that multiplies two arrays element-wise
def multiply_arrays(a, b):
    # Create a result array of the same shape as a and b
    result = np.zeros_like(a)
    
    # Use scipy.weave.inline to execute C code
    code = """
    int i;
    for (i = 0; i < Na[0]; i++) {
        result[i] = a[i] * b[i];
    }
    """
    weave.inline(code, ['a', 'b','result'], 
                 type_converters=weave.converters.blitz, 
                 compiler = 'gcc')
    
    return result

# Test the function
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

result = multiply_arrays(a, b)
print(result)
