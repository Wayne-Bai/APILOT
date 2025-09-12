import numpy as np
from scipy.spatial.distance import jaccard

def kulsinski_dissimilarity(a, b):
    return (np.sum(a & b) - np.sum(a & ~b)) / np.sum(a | b)

# Example usage for 10 pairs of boolean arrays
arrays = [
    (np.array([True, False, True]), np.array([True, True, False])),
    (np.array([False, True, True]), np.array([True, False, True])),
    (np.array([True, True, False]), np.array([False, True, True])),
    (np.array([True, False, False]), np.array([False, False, True])),
    (np.array([False, True, False]), np.array([True, True, False])),
    (np.array([True, True, True]), np.array([False, False, False])),
    (np.array([False, False, True]), np.array([True, False, False])),
    (np.array([True, False, True]), np.array([False, True, True])),
    (np.array([True, True, False]), np.array([True, False, False])),
    (np.array([False, True, True]), np.array([False, True, True]))
]

for i, (array1, array2) in enumerate(arrays):
    dissimilarity = kulsinski_dissimilarity(array1, array2)
    print(f"Kulsinski dissimilarity for pair {i+1}: {dissimilarity}")
