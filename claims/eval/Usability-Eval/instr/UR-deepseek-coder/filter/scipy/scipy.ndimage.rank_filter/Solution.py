import numpy as np
from scipy.ndimage import generic_filter

def rank_filter(data, rank, size):
    def rank_filter_func(values):
        sorted_values = np.sort(values)
        return sorted_values[rank]
    
    return generic_filter(data, rank_filter_func, size=size)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filtered_data = rank_filter(data, rank=1, size=3)
print(filtered_data)
