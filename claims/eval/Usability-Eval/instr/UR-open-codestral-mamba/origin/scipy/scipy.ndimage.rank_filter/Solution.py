import scipy.ndimage
import numpy as np

def multidim_rank_filter(data, size):
    return scipy.ndimage.generic_filter(data, np.median, size=size, mode='constant', cval=0)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filtered_data = multidim_rank_filter(data, size=2)
print(filtered_data)
