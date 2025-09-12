import scipy.integrate as spi
import numpy as np

# Example of using scipy to compile and execute C code on the fly
from scipy import weave

code = """
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += x[i];
    }
    return_val = sum / n;  // Average calculation
"""

# We will use this code to compute the average of an array
def compute_average(arr):
    n = len(arr)
    result = np.zeros(1)
    weave.inline(code, ['x', 'n', 'return_val'], force=1)
    return result[0]

# Example usage
data = np.array([1, 2, 3, 4, 5])
average = compute_average(data)
print("Average:", average)
