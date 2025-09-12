import numpy as np
from scipy.spatial.distance import cdist

def kulsinski_dissimilarity(arr1, arr2):
    # Convert boolean arrays to integer arrays
    arr1 = arr1.astype(int)
    arr2 = arr2.astype(int)

    # Compute components for Kulsinski dissimilarity
    n11 = np.sum(arr1 & arr2)  # count of ones in both vectors
    n10 = np.sum(arr1 & ~arr2) # count of ones in arr1 and zeros in arr2
    n01 = np.sum(~arr1 & arr2) # count of zeros in arr1 and ones in arr2
    
    # Total number of elements in each array
    n = len(arr1)
    
    # Compute the Kulsinski dissimilarity
    dissimilarity = (n10 + n01 - n11 + n) / (n + 1)
    
    return dissimilarity

# Example usage
array1 = np.array([True, False, True, False, True])
array2 = np.array([True, True, False, False, True])
print(kulsinski_dissimilarity(array1, array2))
