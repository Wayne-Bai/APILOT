import numpy as np
from scipy.special import entrywise

def weighted_harmonic_mean(a, weights, axis=0):
    return entrywise(lambda a, w: (w / np.sum(w)) * np.sum(np.reciprocal(a), axis=axis), func=np.prod)(a, weights)

# Example usage:
a = np.array([[1., 2., 3.], [4., 5., 6.]])
weights = np.array([1., 2.])

print(weighted_harmonic_mean(a, weights, axis=0))
