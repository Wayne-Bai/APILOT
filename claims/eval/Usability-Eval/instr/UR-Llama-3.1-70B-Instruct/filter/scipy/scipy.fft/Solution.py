import scipy.fftpack as fft
import numpy as np

# Generate a sample signal
n = 10  # number of samples
t = np.linspace(0, 1, n)  # time array
x = np.sin(2 * np.pi * 5 * t) + 0.3 * np.sin(2 * np.pi * 3 * t) + 0.2 * np.sin(2 * np.pi * 2 * t)

# Compute the 1-D discrete Fourier Transform
X = fft.fft(x)

# Compute the frequencies corresponding to the FFT components
freq = fft.fftfreq(n, d=0.1)  # assuming a sampling period of 0.1

# Print the frequencies and the corresponding FFT components
for f, X_f in zip(freq, X):
    print(f'Frequency: {f:.2f}, Amplitude: {abs(X_f):.4f}, Phase: {np.angle(X_f):.4f}')

# To get the original signal back, use the inverse FFT
x_reconstructed = fft.ifft(X)
print(x_reconstructed)
