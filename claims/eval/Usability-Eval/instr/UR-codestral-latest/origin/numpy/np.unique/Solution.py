import numpy as np

def find_unique_elements(array):
    unique_elements = np.unique(array)
    return np.sort(unique_elements)
