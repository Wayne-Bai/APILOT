import scipy.fft
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
t = np.linspace(0, 1, 100)
x = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Compute the 1-D Discrete Fourier Transform (DFT)
y = np.abs(scipy.fft.fft(x))

# Plot the original signal and its magnitude spectrum
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.subplot(2, 1, 2)
plt.plot(np.linspace(0, 20, len(y)), y)  # Normalize the frequency axis
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()
