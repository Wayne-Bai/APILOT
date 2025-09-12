import scipy.ndimage

def apply_multidimensional_median_filter(data, size=3):
    return scipy.ndimage.median_filter(data, size=size)
