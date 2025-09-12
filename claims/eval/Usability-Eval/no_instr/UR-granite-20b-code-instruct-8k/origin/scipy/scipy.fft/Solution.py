import scipy

def discrete_fourier_transform(signal):
    fourier_transform = scipy.fft.fft(signal)
    return fourier_transform
