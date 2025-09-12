import scipy.special
import numpy as np

# Define a simple C function to be used
code = """
double square(double x) {
    return x * x;
}
"""

# Compile the code
from scipy import weave

# Compile and run the C code
def call_square(x):
    result = np.zeros_like(x, dtype=np.float64)
    weave.inline(code, ['x', 'result'])
    return result

# Test the function
x = np.array([1.0, 2.0, 3.0])
squared_values = call_square(x)
print(squared_values)
