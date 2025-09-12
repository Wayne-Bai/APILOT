import networkx as nx
import numpy as np

def mixing_matrix(G, attribute):
    """
    Returns the numeric mixing matrix for a given attribute in a graph.

    Parameters:
    G (networkx.Graph): The input graph.
    attribute (str): The node attribute to create the mixing matrix for.

    Returns:
    np.ndarray: The numeric mixing matrix.
    """
    # Get the unique values of the attribute
    attribute_values = set(nx.get_node_attributes(G, attribute).values())
    
    # Create a mapping from attribute value to index
    value_to_index = {val: i for i, val in enumerate(attribute_values)}
    
    # Initialize the mixing matrix
    mixing_matrix = np.zeros((len(attribute_values), len(attribute_values)))
    
    # Populate the mixing matrix
    for u, v in G.edges():
        attr_u = nx.get_node_attributes(G, attribute)[u]
        attr_v = nx.get_node_attributes(G, attribute)[v]
        
        if attr_u in value_to_index and attr_v in value_to_index:
            i = value_to_index[attr_u]
            j = value_to_index[attr_v]
            mixing_matrix[i, j] += 1
    
    return mixing_matrix
