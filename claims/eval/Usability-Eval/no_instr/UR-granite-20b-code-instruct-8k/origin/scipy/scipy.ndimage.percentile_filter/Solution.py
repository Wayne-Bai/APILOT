import scipy

def multidimensional_percentile_filter(data, percentile):
    return scipy.stats.percentile_filter(data, percentile, method='gaussian', output='float')
