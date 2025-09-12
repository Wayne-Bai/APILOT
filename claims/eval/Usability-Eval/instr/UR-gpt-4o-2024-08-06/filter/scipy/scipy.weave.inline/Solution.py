import scipy
from scipy import weave
import numpy as np

# Simple example of using scipy.weave to compile C++ code on the fly

# Define an array in Python
array = np.array([1, 2, 3, 4, 5])
n = len(array)

# C++ code to increment each element of the array
code = """
for(int i = 0; i < n; ++i) {
    array[i] += 1;
}
"""

# Execute the C++ code using weave
weave.inline(code, ['array', 'n'])

# Display the modified array
print(array)
