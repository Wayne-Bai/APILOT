import scipy
from scipy import weave

# Example C code for a simple function to add two numbers
code = r"""
double add_numbers(double a, double b) {
    return a + b;
}
"""

# Create a Python wrapper for the C code
def add(a, b):
    result = weave.inline(code, ['a', 'b'])
    return result

# Example usage
result = add(3.0, 4.5)
print("The result of adding 3.0 and 4.5 is:", result)
