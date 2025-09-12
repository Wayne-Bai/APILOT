import numpy as np

def find_common_type(a, b):
    dtype_a = np.asarray(a).dtype
    dtype_b = np.asarray(b).dtype
    if dtype_a == dtype_b:
        return dtype_a
    if dtype_a.kind < dtype_b.kind:
        return dtype_b
    return dtype_a

a = [1, 2, 3.3]
b = [4.1, 5, 6]
common_type = find_common_type(a, b)
common_type
