import numpy as np
from scipy.signal import gaussian

def gaussian_filter1d(x, sigma):
    n = len(x)
    k = int(np.ceil(6 * sigma))
    kernel = gaussian(k, sigma)
    kernel = kernel / np.sum(kernel)
    y = np.convolve(x, kernel, mode='same')

    return y
