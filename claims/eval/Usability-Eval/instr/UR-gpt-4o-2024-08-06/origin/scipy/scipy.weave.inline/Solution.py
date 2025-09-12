import scipy
from scipy import weave
from scipy.weave import converters

# Define C++ code as a string
cpp_code = """
int square(int x) {
    return x * x;
}
"""

# Compile and execute the C++ code using inline
def calculate_square(n):
    result = weave.inline(cpp_code,
                          ['n'],
                          compiler='gcc',
                          type_converters=converters.blitz)
    return result

# Test the compiled function
print(calculate_square(5))
