import numpy as np

def test_all_along_axis(array, axis):
    return np.all(array, axis=axis)
