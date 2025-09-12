import scipy

def calculate_weighted_harmonic_mean(data, weights, axis):
    return scipy.hmean(data, weights, axis)
