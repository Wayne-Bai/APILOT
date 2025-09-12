import numpy as np
from scipy.fft import fft

# Define a 1D array
x = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# Compute the 1-D discrete Fourier Transform
xf = fft(x)

print(xf)
