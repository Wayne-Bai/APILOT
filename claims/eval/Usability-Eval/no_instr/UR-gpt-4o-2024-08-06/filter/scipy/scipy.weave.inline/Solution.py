import numpy as np
from scipy import weave

# Define a simple C++ code as a string
cpp_code = """
int size = Nx[0];
for (int i = 0; i < size; i++) {
    y(i) = 2 * x(i);
}
"""

# Prepare input data
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.zeros_like(x)

# Execute the C++ code
weave.inline(cpp_code, ['x', 'y'])

# Output the modified y
print("Output array:", y)
