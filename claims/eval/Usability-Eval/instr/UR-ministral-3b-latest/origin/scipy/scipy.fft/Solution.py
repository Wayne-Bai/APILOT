import scipy.signal
import numpy as np

# Creating a sample signal
x = np.sin(2 * np.pi * 3 * np.linspace(0, 1, 1000))

# Computing the 1-D discrete Fourier Transform
frequencies, spectrum = scipy.signal.dft(x)

# Print the results
print(f"Frequencies: {frequencies}")
print(f"Spectrum: {spectrum}")
