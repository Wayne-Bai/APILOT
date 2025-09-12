import numpy as np

def test_any_array_element(array, axis):
    return np.any(array, axis=axis)
