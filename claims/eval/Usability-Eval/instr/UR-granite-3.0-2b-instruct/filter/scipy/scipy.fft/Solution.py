import numpy as np
from scipy.fft import fft, fftfreq

# Generate a signal
t = np.linspace(0, 1, 1000)  # time vector from 0 to 1 second with 1000 points
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)  # a sum of two sine waves

# Compute the 1-D discrete Fourier Transform
fourier_transform = fft(signal)

# Compute the frequency vector
frequencies = fftfreq(len(signal), t[1] - t[0])

# Print the Fourier Transform and the frequencies
print("Fourier Transform:", fourier_transform)
print("Frequencies:", frequencies)
