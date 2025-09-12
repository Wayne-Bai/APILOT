# Import the necessary scipy library
from scipy.fft import fft, fftfreq

# Define the function to compute 1-D discrete Fourier Transform
def compute_dft(signal):
    """
    Compute the 1-D discrete Fourier Transform of a given signal.

    Parameters:
    signal (array): The input signal to be transformed.

    Returns:
    fft_out (array): The output of the 1-D discrete Fourier Transform.
    freq (array): The frequencies corresponding to the output of the 1-D discrete Fourier Transform.
    """

    # Calculate the discrete Fourier Transform of the signal
    fft_out = fft(signal)

    # Calculate the frequencies corresponding to the output of the discrete Fourier Transform
    freq = fftfreq(len(signal), d=1)

    return fft_out, freq

# Generate an example signal
import numpy as np
signal = np.sin(2 * np.pi * 5 * np.arange(100)) + 0.5 * np.sin(2 * np.pi * 10 * np.arange(100))

# Compute the 1-D discrete Fourier Transform
dft_out, freq = compute_dft(signal)

# Print the results
print("Input Signal: ", signal)
print("Frequencies: ", freq)
print("1-D Discrete Fourier Transform: ", dft_out)
