import numpy as np
from scipy.fftpack import fft

# Example input signal
x = np.array([1, 2, 3, 4])

# Compute the 1-D discrete Fourier Transform
X = fft(x)

print("Input signal:", x)
print("discrete Fourier Transform:", X)
