from scipy.ndimage import generic_filter

def max_filter(input_array, size, footprint=None):
    if footprint is None:
        footprint = np.ones((size,) * input_array.ndim)
    return generic_filter(input_array, np.max, size=size, footprint=footprint)
