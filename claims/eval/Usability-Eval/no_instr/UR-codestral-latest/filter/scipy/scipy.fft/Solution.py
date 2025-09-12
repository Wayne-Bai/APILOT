# Import the necessary packages
import numpy as np
from scipy.fft import fft

# Let's generate a simple 1-D array for demonstration
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

# Compute the 1-D discrete Fourier Transform
xf = fft(x)

# Print the result
print("Discrete Fourier Transform of the array:")
print(xf)
