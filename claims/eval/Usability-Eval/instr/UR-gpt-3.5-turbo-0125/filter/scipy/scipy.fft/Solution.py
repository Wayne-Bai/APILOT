
import numpy as np

def compute_discrete_fourier_transform(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    transform = np.dot(W, signal)
    return transform

# Example Usage
signal = np.array([0, 1, 2, 3, 4, 5, 6, 7])
transformed_signal = compute_discrete_fourier_transform(signal)
print("1-D Discrete Fourier Transform:", transformed_signal)
