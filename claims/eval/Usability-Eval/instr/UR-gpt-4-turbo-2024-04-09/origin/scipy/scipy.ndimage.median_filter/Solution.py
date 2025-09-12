import scipy.ndimage

def apply_multidimensional_median_filter(data, size):
    filtered_data = scipy.ndimage.median_filter(data, size=size)
    return filtered_data
