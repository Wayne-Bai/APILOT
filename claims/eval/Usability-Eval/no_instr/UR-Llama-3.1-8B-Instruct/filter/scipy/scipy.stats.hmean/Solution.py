import scipy

def weighted_harmonic_mean(arr, w):
    """
    Calculate the weighted harmonic mean along the specified axis.

    Parameters:
    - arr (array_like): input array.
    - w (array_like): weights for the input array.

    Returns:
    - weighted mean (array_like): the weighted harmonic mean of the input array.
    """
    # Ensure input arrays have the same shape
    assert arr.shape == w.shape, "Input arrays must have the same shape"

    # Clip the weights to be between 0 and 1
    w = np.clip(w, 0, 1)

    # Calculate the weighted harmonic mean
    harmonic_mean = np.sum(w / arr) / np.sum(w)

    return harmonic_mean

import numpy as np
import scipy
from scipy import stats

# Example usage:
arr = np.array([[1, 2, 3], [4, 5, 6]])
w = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

print(weighted_harmonic_mean(arr, w))
