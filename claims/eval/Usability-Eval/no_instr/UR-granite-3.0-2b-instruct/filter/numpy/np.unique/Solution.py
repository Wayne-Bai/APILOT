import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    sorted_unique_elements = np.sort(unique_elements)
    return sorted_unique_elements
