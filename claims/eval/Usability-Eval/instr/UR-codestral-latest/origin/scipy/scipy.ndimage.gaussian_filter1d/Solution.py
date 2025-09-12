import numpy as np
from scipy.ndimage import gaussian_filter1d

def gaussian_filter(signal, std_dev):
    filtered_signal = gaussian_filter1d(signal, std_dev)
    return filtered_signal
