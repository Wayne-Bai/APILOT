import scipy.weave

# Here is an example of how to use scipy.weave to compile and execute C++ code
code = """
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""

scipy.weave.inline(code, compiler='gcc')
