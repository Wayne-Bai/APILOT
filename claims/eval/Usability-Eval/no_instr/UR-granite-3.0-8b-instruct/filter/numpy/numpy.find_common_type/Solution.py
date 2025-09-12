import numpy as np

def common_type(arr1, arr2):
    # Determine the common data type following standard coercion rules
    common_type = np.common_type(arr1, arr2)
    return common_type
