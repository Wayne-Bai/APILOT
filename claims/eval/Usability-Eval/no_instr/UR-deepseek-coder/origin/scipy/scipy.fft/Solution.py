import numpy as np
from scipy.fft import fft

# Example data
data = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

# Compute the 1-D discrete Fourier Transform
fft_result = fft(data)

print("Fourier Transform result:", fft_result)
