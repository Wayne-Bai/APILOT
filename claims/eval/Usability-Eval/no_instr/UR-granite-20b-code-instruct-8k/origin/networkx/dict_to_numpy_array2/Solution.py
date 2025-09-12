import numpy as np
import networkx as nx

def dict_to_2d_array(d, mapping=None):
    """Convert a dictionary of dictionaries to a 2d numpy array with optional mapping.

    Parameters
    ----------
    d : dict of dicts
        The input dictionary of dictionaries.
    mapping : list, optional
        A list of keys to use as the mapping for the array. If not provided, the keys will be sorted alphabetically.

    Returns
    -------
    numpy.ndarray
        2d numpy array representing the input dictionary of dictionaries.
    """
    if mapping is None:
        mapping = sorted(d.keys())
    arr = np.empty((len(mapping), len(mapping)), dtype=object)
    for i, k1 in enumerate(mapping):
        for j, k2 in enumerate(mapping):
            arr[i, j] = d[k1].get(k2)
    return arr
