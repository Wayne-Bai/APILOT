import scipy.fftpack as fft
import numpy as np

# Define a 1D array
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# Compute the 1-D discrete Fourier Transform
X = fft.fft(x)

# Print the result
print("Original array:")
print(x)
print("\n1-D discrete Fourier Transform:")
print(X)

# Compute the inverse 1-D discrete Fourier Transform
x_reconstructed = fft.ifft(X)

# Print the result
print("\nReconstructed original array:")
print(x_reconstructed)
