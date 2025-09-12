import numpy as np

def test_array(array, axis=None):
    return np.all(array, axis=axis)
