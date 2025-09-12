import numpy as np
from scipy.fftpack import fft

# Generate sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + 0.5 * np.cos(2 * x)

# Compute Fourier transform
X = fft(y)

# Print the resulting complex-valued array X
print(X)
