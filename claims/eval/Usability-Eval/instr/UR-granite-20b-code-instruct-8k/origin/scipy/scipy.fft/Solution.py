import scipy.fftpack

def compute_1d_dft(x):
    return scipy.fftpack.fft(x)
