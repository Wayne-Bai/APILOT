
import networkx as nx

def convert_dict_to_numpy_array(input_dict, mapping=None):
    """
    Convert a dictionary of numbers to a 1D numpy array with optional mapping.

    Parameters
    ----------
    input_dict : dict
        A dictionary of numbers.
    mapping : dict, optional
        A mapping dictionary to map the keys of the input dictionary to the array indices.

    Returns
    -------
    numpy.ndarray
        1D numpy array of the values from the input dictionary.
    """
    g = nx.convert_matrix.from_dict_of_numbers(input_dict, mapping=mapping)
    return nx.convert_matrix.to_numpy_array(g)
