import scipy.fft

# Define a sample input signal, a simple numpy array
signal = [0, 1, 0, -1]

# Compute the 1-D discrete Fourier Transform
dft_output = scipy.fft.fft(signal)

# Output the result
print(dft_output)
