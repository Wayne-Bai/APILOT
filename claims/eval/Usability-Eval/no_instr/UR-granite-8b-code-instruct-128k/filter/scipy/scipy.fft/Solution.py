from scipy.fft import fft
import numpy as np
# Generate a random input array
x = np.random.random(10)
# Compute the 1-D discrete Fourier Transform
X = fft(x)
# Print the result
print(X)
