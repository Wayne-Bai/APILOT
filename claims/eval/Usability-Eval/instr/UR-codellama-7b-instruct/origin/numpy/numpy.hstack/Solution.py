
import numpy as np

def stack_arrays(arrays):
    # Check if input is a list of arrays
    if not isinstance(arrays, list):
        raise ValueError("Input must be a list of arrays")
    
    # Get the shape of the first array in the list
    shape = np.shape(arrays[0])
    
    # Check if all arrays have the same number of dimensions and shape
    for array in arrays:
        if not isinstance(array, np.ndarray):
            raise ValueError("All input arrays must be numpy arrays")
        if np.shape(array) != shape:
            raise ValueError("All input arrays must have the same number of dimensions and shape")
    
    # Create an empty array to store the stacked arrays
    stacked_arrays = np.empty((0, shape[1]))
    
    # Iterate through the list of arrays and add each array to the stacked arrays
    for array in arrays:
        stacked_arrays = np.append(stacked_arrays, array, axis=0)
    
    return stacked_arrays
