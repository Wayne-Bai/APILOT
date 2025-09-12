
import numpy as np
from itertools import zip_longest

def assertEqual(a, b, tol=1e-5):
    if not isinstance(a, (list, tuple)):
        raise ValueError("'a' must be a list or tuple")
    if not isinstance(b, (list, tuple)):
        raise ValueError("'b' must be a list or tuple")
    if len(a) != len(b):
        raise ValueError("'a' and 'b' must have the same length")
    for i in range(len(a)):
        if abs(a[i] - b[i]) > tol:
            raise AssertionError(f"Elements at index {i} are not equal: {a[i]} != {b[i]}")
