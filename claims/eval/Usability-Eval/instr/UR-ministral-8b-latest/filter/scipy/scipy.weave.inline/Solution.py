import scipy.special
from scipy import *  # Importing the full scipy namespace

# Define a simple C/C++ function
source_code = '''
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}
'''

# Compile the C/C++ code
exec = compile(source_code, '<string>', 'exec')

# Define a wrapper function
def add(a, b):
    func = exec.globals['add']
    return func(a, b)

# Test the function
result = add(3, 4)
print(f"The result of adding 3 and 4 is: {result}")
