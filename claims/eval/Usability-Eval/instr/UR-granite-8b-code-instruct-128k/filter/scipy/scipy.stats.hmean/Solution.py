import scipy.stats

def calculate_weighted_harmonic_mean(data, weights, axis):
    return scipy.stats.mstats.weighted_harmonic_mean(data, weights, axis)
