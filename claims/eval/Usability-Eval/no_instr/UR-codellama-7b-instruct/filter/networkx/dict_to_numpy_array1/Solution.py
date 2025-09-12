
import numpy as np

def dict_to_array(dict, mapping=None):
    """
    Convert a dictionary of numbers to a 1d numpy array with optional mapping.
    
    Args:
        dict (dict): Dictionary of numbers to convert.
        mapping (function): Optional function to apply to each value in the dictionary before converting it to an array.
    
    Returns:
        ndarray: Numpy array containing the converted dictionary values.
    """
    if not isinstance(dict, dict):
        raise ValueError("'dict' must be a dictionary.")

    # Get list of keys and values from dictionary
    keys = list(dict.keys())
    vals = list(dict.values())

    # Apply mapping function to values if provided
    if mapping is not None:
        vals = [mapping(v) for v in vals]

    # Create numpy array from list of values
    arr = np.array(vals)

    return arr
