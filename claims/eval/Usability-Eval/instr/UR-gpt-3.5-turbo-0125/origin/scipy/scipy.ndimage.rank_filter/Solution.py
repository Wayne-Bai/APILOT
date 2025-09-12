
import numpy as np
from scipy.ndimage import generic_filter

def rank_filter(data, size, rank):
    def rank_func(arr):
        return np.sort(arr)[rank]

    result = generic_filter(data, rank_func, size=size)
    return result

# Example usage
data = np.random.randint(0, 100, (10, 10))
size = 3
rank = 4
filtered_data = rank_filter(data, size, rank)
print(filtered_data)
