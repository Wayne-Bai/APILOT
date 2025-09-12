import numpy as np
from scipy.fft import fft

# Sample data
data = np.array([1, 2, 3, 4])

# Compute the 1-D discrete Fourier Transform
fft_result = fft(data)

# Print the result
print(fft_result)
