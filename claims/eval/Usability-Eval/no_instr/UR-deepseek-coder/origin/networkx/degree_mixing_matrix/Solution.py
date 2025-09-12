import networkx as nx
import numpy as np

def attribute_mixing_matrix(G, attribute, normalized=True):
    """
    Returns the mixing matrix for the given attribute.

    Parameters:
    G (networkx.Graph): The graph to analyze.
    attribute (str): The node attribute to consider for mixing.
    normalized (bool): Whether to normalize the mixing matrix.

    Returns:
    numpy.ndarray: The mixing matrix.
    """
    # Get the attribute values for all nodes
    attr_values = nx.get_node_attributes(G, attribute)
    
    # Get the unique attribute values
    unique_values = set(attr_values.values())
    
    # Initialize the mixing matrix
    mixing_matrix = np.zeros((len(unique_values), len(unique_values)))
    
    # Create a mapping from attribute values to matrix indices
    value_to_index = {value: i for i, value in enumerate(unique_values)}
    
    # Fill the mixing matrix
    for u, v in G.edges():
        attr_u = attr_values[u]
        attr_v = attr_values[v]
        mixing_matrix[value_to_index[attr_u], value_to_index[attr_v]] += 1
        if u != v:  # If not a self-loop, count the reverse edge as well
            mixing_matrix[value_to_index[attr_v], value_to_index[attr_u]] += 1
    
    # Normalize the mixing matrix if requested
    if normalized:
        row_sums = mixing_matrix.sum(axis=1, keepdims=True)
        mixing_matrix = np.divide(mixing_matrix, row_sums, out=np.zeros_like(mixing_matrix), where=row_sums!=0)
    
    return mixing_matrix
