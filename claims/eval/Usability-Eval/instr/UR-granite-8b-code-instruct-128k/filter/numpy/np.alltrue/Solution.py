import numpy as np

def test_all_along_axis(arr, axis):
    return np.all(arr, axis=axis)
