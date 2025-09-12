import scipy

# Example C code to be compiled and executed
c_code = """
#include <stdio.h>

void hello_world() {
    printf("Hello, World from C!\\n");
}
"""

# Compile and execute the C code using scipy
compiled_code = scipy.weave.inline(c_code, [], compiler='gcc')

# Call the compiled function
compiled_code.hello_world()
