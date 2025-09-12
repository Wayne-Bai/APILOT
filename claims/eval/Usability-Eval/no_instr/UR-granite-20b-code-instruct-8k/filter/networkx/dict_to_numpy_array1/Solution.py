import numpy as np
import networkx as nx

def convert_dict_to_numpy_array(input_dict, mapping=None):
    """Convert a dictionary of numbers to a 1d numpy array with optional mapping.
    
    Parameters
    ----------
    input_dict : dict
        Dictionary of numbers to be converted.
    mapping : dict, optional
        Optional mapping of input values to array indices. Default is None.
    
    Returns
    -------
    numpy.ndarray
        Converted 1d numpy array.
    """
    if mapping is None:
        mapping = {val: i for i, val in enumerate(input_dict.keys())}
    arr = np.zeros(len(mapping))
    for key, val in input_dict.items():
        arr[mapping[key]] = val
    return arr
