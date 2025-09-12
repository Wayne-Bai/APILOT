
import numpy as np
from scipy.stats import hmean

def calculate_weighted_harmonic_mean(data, weights=None, axis=0):
    # Calculate the weighted harmonic mean along the specified axis
    if weights is None:
        weights = np.ones(data.shape[axis]) / data.shape[axis]
    return hmean(data, weights)
