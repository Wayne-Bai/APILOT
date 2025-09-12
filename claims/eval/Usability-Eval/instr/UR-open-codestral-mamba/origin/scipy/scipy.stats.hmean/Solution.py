import scipy.stats as stats

def calculate_weighted_harmonic_mean(data, axis, weights):
    # Using the scipy.stats.hmean function
    weighted_data = data * weights
    hmean = stats.hmean(weighted_data, axis=axis)
    return hmean
