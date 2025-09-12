
import numpy as np

def determine_common_type(a, b):
    # If either of the inputs is a list or tuple, convert them to arrays
    if isinstance(a, (list, tuple)):
        a = np.array(a)
    if isinstance(b, (list, tuple)):
        b = np.array(b)
    
    # Determine the common type by finding the highest precedence data type in a and b
    a_type = a.dtype
    b_type = b.dtype
    if a_type == b_type:
        return a_type
    else:
        # Find the higher precedence data type
        higher_precedence = np.array([a, b]).dtype
        return higher_precedence
