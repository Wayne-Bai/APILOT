import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

# Define input signal
N = 2048 # Number of samples in the signal
x = np.linspace(0, 1, N) + 0.5 # Generate sample points for the sine wave signal
xfreq = 32/N # Frequency of the oscillation
amp = 10 # Amplitude of the signal

# Define the sine wave signal
y = amp * np.sin(2 * np.pi * xfreq * x)

# Compute the 1-D discrete Fourier Transform (DFT) using SciPy
X = fft(y) # Perform the DFT

# Plot the magnitude of the DFT
plt.plot(np.abs(X))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum of Discrete Fourier Transform (DFT)')
plt.show()