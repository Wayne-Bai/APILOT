import scipy.ndimage

def apply_multidimensional_gaussian_filter(data, sigma=1):
    return scipy.ndimage.gaussian_filter(data, sigma)
