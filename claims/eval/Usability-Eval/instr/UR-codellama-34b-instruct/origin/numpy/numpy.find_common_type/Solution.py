
import numpy as np

def find_common_type(a, b):
    # If either input is a scalar, return the type of the other input.
    if np.isscalar(a) or np.isscalar(b):
        return np.asarray(b).dtype if np.isscalar(a) else np.asarray(a).dtype
    
    # If both inputs are arrays, find the common type among their elements.
    else:
        return np.find_common_type([np.asarray(a).dtype, np.asarray(b).dtype])
