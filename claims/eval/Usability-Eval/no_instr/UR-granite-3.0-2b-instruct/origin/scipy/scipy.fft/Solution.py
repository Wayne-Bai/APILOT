from scipy.fftpack import fft, ifft
import numpy as np

# Generate a signal
signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# Compute the 1-D discrete Fourier Transform
fourier_transform = fft(signal)

# Compute the inverse Fourier Transform
inverse_fourier_transform = ifft(fourier_transform)

# Print the original signal and the inverse Fourier Transform
print("Original Signal:")
print(signal)
print("\nInverse Fourier Transform:")
print(inverse_fourier_transform)
