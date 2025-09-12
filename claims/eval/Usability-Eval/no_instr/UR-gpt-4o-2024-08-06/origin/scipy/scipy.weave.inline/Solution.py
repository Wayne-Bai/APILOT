import numpy as np
from scipy import weave

# Define a simple C code function as a string
c_code = """
double square_sum(int n, double *x) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += x[i] * x[i];
    }
    return result;
}
"""

# Example Python array
x = np.array([1.0, 2.0, 3.0, 4.0], dtype='double')

# Compile and execute the C code
result = weave.inline(c_code, ['x'], type_converters=weave.converters.blitz)

print("The sum of squares is:", result)
