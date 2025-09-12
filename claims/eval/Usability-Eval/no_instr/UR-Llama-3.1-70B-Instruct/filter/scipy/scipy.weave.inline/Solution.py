import scipy
from scipy.weave import inline

# Define a simple C function using scipy's weave.inline function
# This function calculates the value of x squared plus y
code = """
int square(int x, int y) {
    return x*x + y;
}
"""

# Compile the C code on the fly
square_func = inline(code, ['x', 'y'])

# Use the compiled function
print(square_func(2, 3))  # Expected output: 7
