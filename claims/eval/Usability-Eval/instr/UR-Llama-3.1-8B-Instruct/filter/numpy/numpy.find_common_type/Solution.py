import numpy as np

def determine_common_type(*args):
    """
    Determine the common type following standard coercion rules.
    """
    types = set(type(arg) for arg in args)
    
    # Determine the numerical types first
    numerical_types = {np.int32, np.int64, np.float16, np.float32, np.float64}
    if any(t in types for t in numerical_types):
        # Prioritize np.float64 over other numerical types
        if np.float64 in types:
            return np.float64
        else:
            return min(types & numerical_types, key=lambda x: np.finfo(x).precision)
    
    # Prioritize np.bool_ over other types
    if np.bool_ in types:
        return np.bool_
    
    # Determine the string type
    if any(isinstance(arg, str) for arg in args):
        return str
    
    # Determine the byte string type
    if any(isinstance(arg, bytes) for arg in args):
        return bytes
    
    # The type is always object, because all other types are a subclass of object
    return object

# Example usage:
print(determine_common_type(1, 1.0, True))  # Output: <class 'float'>
