import numpy as np
from scipy.fft import fft

def compute_discrete_fourier_transform(signal):
    """
    Compute the 1-D discrete Fourier Transform of a given signal.

    Parameters:
    signal (numpy array): Input signal for the Fourier Transform.

    Returns:
    numpy array: Complex-valued spectrum of the input signal.
    """
    # Compute the Fourier Transform
    fft_signal = fft(signal)

    return fft_signal

# Example usage:
if __name__ == "__main__":
    # Generate a sample signal
    sample_signal = np.array([1, 2, 3, 4, 5])

    # Compute and print the discrete Fourier Transform
    fft_signal = compute_discrete_fourier_transform(sample_signal)
    print("Discrete Fourier Transform of the sample signal: ", fft_signal)

