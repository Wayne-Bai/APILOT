from scipy import ctypes

# Define the function in C that you want to optimize.
code = """
double func(double x) {
    return 3.0 * x + 1;
}
"""

# Compile the C function.
func_ = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(code)

# Use the compiled function as a Python function.
print(func_(2.0))
