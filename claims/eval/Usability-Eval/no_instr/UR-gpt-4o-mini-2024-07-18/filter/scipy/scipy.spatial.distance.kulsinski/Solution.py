import numpy as np
from scipy.spatial.distance import pdist, squareform

def kulsinski_dissimilarity(arr1, arr2):
    # Convert the boolean arrays to integers
    arr1 = arr1.astype(int)
    arr2 = arr2.astype(int)
    # Stack the arrays for pdist
    stacked = np.vstack((arr1, arr2))
    # Calculate the Kulsinski dissimilarity
    dissimilarity = pdist(stacked, metric='kulsinski')
    return dissimilarity[0]

# Example boolean arrays
bool_array1 = np.array([True, False, True, False, True])
bool_array2 = np.array([False, True, True, True, False])

# Compute Kulsinski dissimilarity
dissimilarity_value = kulsinski_dissimilarity(bool_array1, bool_array2)
print(f"Kulsinski Dissimilarity: {dissimilarity_value}")
