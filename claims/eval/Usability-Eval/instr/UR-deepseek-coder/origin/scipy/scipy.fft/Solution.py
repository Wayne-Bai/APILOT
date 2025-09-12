import numpy as np
from scipy.fft import fft

# Example usage
signal = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
fourier_transform = fft(signal)

print(fourier_transform)
