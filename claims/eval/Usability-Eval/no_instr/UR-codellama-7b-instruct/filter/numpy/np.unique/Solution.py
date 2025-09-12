
import numpy as np

def unique(arr):
    # Get the sorted indices of the array
    indices = np.sort(np.unique(arr))

    # Return the sorted unique elements of the array
    return arr[indices]
