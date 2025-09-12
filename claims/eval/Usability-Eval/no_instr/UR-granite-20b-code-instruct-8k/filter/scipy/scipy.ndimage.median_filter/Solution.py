from scipy import ndimage

def multidimensional_median_filter(input_array, size):
    return ndimage.median_filter(input_array, size=size)
