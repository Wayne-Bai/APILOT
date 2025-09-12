from scipy.stats import hmean

def calculate_weighted_harmonic_mean(data, weights, axis=-1):
    if len(data.shape) > 1:
        data = data.ravel()
        weights = weights.ravel()
    return hmean(data, weights=weights, axis=axis)
