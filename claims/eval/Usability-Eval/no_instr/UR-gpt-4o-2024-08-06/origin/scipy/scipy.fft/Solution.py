import numpy as np
from scipy.fft import fft

# Sample data: a simple sine wave
x = np.linspace(0.0, 1.0, 500)
y = np.sin(50.0 * 2.0 * np.pi * x)

# Compute the 1-D discrete Fourier Transform
y_fft = fft(y)

# Display the results
print("Input Signal:")
print(y)
print("\nFourier Transform:")
print(y_fft)
