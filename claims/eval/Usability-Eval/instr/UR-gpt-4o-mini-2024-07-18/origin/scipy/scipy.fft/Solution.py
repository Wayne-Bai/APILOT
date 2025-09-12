
import scipy.fft

# Sample data (1-D array)
data = [1, 2, 3, 4]

# Compute the 1-D discrete Fourier Transform
dft_result = scipy.fft.fft(data)

print(dft_result)
