import scipy.fft

# Example data
data = [1, 2, 3, 4, 5]

# Compute the 1-D discrete Fourier Transform
dft_result = scipy.fft.fft(data)

print(dft_result)
