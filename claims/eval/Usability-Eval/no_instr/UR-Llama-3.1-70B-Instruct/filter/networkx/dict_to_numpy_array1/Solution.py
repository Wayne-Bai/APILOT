import networkx as nx
import numpy as np

def dict_to_numpy_array(dictionary, mapping=None):
    """
    Convert a dictionary of numbers to a 1D numpy array with optional mapping.

    Args:
    dictionary (dict): Dictionary of numbers to convert.
    mapping (dict, optional): Optional mapping to apply to dictionary values. Defaults to None.

    Returns:
    numpy.ndarray: 1D numpy array of dictionary values with optional mapping applied.
    """

    # Create a new empty graph
    G = nx.Graph()

    # Add nodes to the graph for each key in the dictionary
    for key in dictionary:
        G.add_node(key)

    # Add node attributes to the graph for each key-value pair in the dictionary
    nx.set_node_attributes(G, dictionary, 'value')

    # Get the node attributes (i.e., the dictionary values) as a list
    node_values = [G.nodes[node].get('value') for node in G.nodes()]

    # If a mapping is provided, apply it to the node values
    if mapping is not None:
        node_values = [mapping.get(value, value) for value in node_values]

    # Convert the list of node values to a 1D numpy array
    numpy_array = np.array(node_values)

    return numpy_array

# Example usage:
dictionary = {'a': 1, 'b': 2, 'c': 3}
mapping = {1: 10, 2: 20, 3: 30}

result = dict_to_numpy_array(dictionary, mapping)
print(result)  # Output: [10 20 30]
