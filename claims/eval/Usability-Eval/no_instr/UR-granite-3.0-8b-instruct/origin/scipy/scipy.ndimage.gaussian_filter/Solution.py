import numpy as np
from scipy.ndimage import gaussian_filter

def multidimensional_gaussian_filter(image, sigma):
    return gaussian_filter(image, sigma, mode='nearest')
