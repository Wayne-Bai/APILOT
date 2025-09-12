import scipy.signal  # Importing scipy.signal which includes methods for signal processing

# Example usage:
# Signal to transform
signal = [1, 2, 3, 4, 5]

# Compute the 1-D discrete Fourier Transform
fourier_transform = scipy.signal.fft(signal)

print("Discrete Fourier Transform:", fourier_transform)
