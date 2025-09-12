import scipy.fftpack

def compute_discrete_fourier_transform(signal):
    # compute the 1-D discrete Fourier Transform of the signal
    fourier_transform = scipy.fftpack.fft(signal)
    return fourier_transform

# Let's test the function with an example signal
signal = [1, 2, 3, 4, 5]
print(compute_discrete_fourier_transform(signal))
