import numpy as np

def find_common_type(array1, array2):
    common_type = np.find_common_type([array1, array2], [])
    return common_type
