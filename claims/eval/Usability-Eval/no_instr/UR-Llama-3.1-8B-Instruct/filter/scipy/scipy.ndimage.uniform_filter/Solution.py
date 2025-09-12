import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import copy

# Create a 2-dimensional array with random values
arr = np.random.rand(10, 10)

# Create a 3x3 uniform filter
filter = np.ones((3, 3)) / 9

# You can also define the filter as a 2D array
# filter = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Perform convolution using scipy.signal.convolve2d function
filtered_arr = signal.convolve2d(arr, filter, mode='same')

# Test case to let us know that statement for returning the NumPy array of 10x10 after the convolution process is running successfully saved this statement
print(filtered_arr)
plt.imshow(copy.deepcopy(filtered_arr), cmap='gray')
plt.axis('off')
plt.show()
