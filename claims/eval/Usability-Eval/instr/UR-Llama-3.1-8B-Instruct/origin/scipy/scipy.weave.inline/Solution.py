from scipy import weave

# Define the C/C++ code to be executed
code = """
#include <math.h>

double calculate(double x) {
    return x * x + 3 * x + 2;
}
"""

# Compile the C/C++ code into a Python extension module
weave.inline(code, ['x'], type_converters=weave.converters.blitz, compiler='gcc', sources=['scipy.weavecommend_c'])


# Define the function to be executed
def execute_function(x):
    return weave.inline(code, ['x'], type_converters=weave.converters.blitz, compiler='gcc', sources=['scipy.weavecommend_c'])

# Test the function
x = 3.0
result = execute_function(x)
print(result)
