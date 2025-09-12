import numpy as np
from scipy.fft import fft

# Assume x is your input signal
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Compute the 1-D discrete Fourier Transform
fft_result = fft(x)

# Print the result
print(fft_result)
