import numpy as np
import ctypes

def get_strides_ctypes_array(arr):
    # Get the shape and strides of the array
    shape = arr.shape
    strides = arr.strides
    
    # Determine the base type for the shape attribute
    base_type = ctypes.c_intp
    
    # Create a ctypes array of length self.ndim with the base type
    strides_ctypes_array = (base_type * len(shape))(*strides)
    
    return strides_ctypes_array

# Example usage
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
strides_ctypes_array = get_strides_ctypes_array(arr)
print(strides_ctypes_array)
