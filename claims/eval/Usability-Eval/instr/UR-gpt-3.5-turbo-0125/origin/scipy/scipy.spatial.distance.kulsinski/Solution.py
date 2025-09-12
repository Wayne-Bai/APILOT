
import numpy as np

def kulsinski_dissimilarity(arr1, arr2):
    n = len(arr1)
    agree = sum((arr1[i] != arr2[i]) for i in range(n))
    disagree = sum((arr1[i] == 1 and arr2[i] == 0) for i in range(n))
    if disagree == 0:
        return 1.0
    return disagree / (disagree + 2 * agree)

# Example usage
arr1 = np.array([True, False, True, True, False])
arr2 = np.array([True, True, False, True, False])

print(kulsinski_dissimilarity(arr1, arr2))
