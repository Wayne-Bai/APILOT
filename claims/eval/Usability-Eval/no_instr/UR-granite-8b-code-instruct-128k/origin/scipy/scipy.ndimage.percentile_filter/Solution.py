import scipy

def percentile_filter(data, percentile):
    filtered_data = scipy.ndimage.percentile_filter(data, percentile, size=(3, 3))
    return filtered_data
