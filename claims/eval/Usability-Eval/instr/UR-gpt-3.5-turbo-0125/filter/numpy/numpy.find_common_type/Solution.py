
import numpy as np

def find_common_type(types):
    try:
        return np.find_common_type(types, [])
    except TypeError:
        return None

types = [np.dtype('int32'), np.dtype('float64')]
common_type = find_common_type(types)
print(common_type)
