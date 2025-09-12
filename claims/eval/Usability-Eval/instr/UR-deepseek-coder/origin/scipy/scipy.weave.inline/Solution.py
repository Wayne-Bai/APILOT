import scipy.weave as weave

# Example C++ code to be compiled and executed
cpp_code = """
#include <iostream>

void hello_world() {
    std::cout << "Hello, World from C++!" << std::endl;
}
"""

# Function to compile and execute the C++ code
def run_cpp_code():
    weave.inline(cpp_code, [], compiler='gcc')

# Run the C++ code
run_cpp_code()
