import numpy as np
from scipy import ndimage

def percentile_filter(input_array, percentile):
    return ndimage.percentile_filter(input_array, percentile)
