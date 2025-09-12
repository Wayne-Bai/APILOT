import networkx as nx
import numpy as np

def mixing_matrix(G, attribute):
    """
    Returns mixing matrix for attribute.
    
    Parameters
    ----------
    G : networkx Graph
    attribute : node attribute key
    
    Returns
    -------
    m : numpy array
       Mixing matrix. m[i,j] is the fraction of nodes of type i that are connected to nodes of type j.
    
    Notes
    -----
    Each row of m sums to 1.
    """
    
    # Get all unique attribute values
    attribute_values = set(nx.get_node_attributes(G, attribute).values())
    
    # Initialize mixing matrix
    m = np.zeros((len(attribute_values), len(attribute_values)))
    
    # Get attribute value for each node
    node_attributes = nx.get_node_attributes(G, attribute)
    
    # Calculate mixing matrix
    for u, v in G.edges():
        u_attribute = node_attributes[u]
        v_attribute = node_attributes[v]
        
        # Get indices for attribute values
        u_index = list(attribute_values).index(u_attribute)
        v_index = list(attribute_values).index(v_attribute)
        
        # Increment mixing matrix
        m[u_index, v_index] += 1
        
    # Normalize mixing matrix
    m = m / m.sum(axis=1, keepdims=True)
    
    return m

# Example usage:
G = nx.Graph()
G.add_nodes_from([1, 2, 3], type='A')
G.add_nodes_from([4, 5, 6], type='B')
G.add_edges_from([(1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6)])

m = mixing_matrix(G, 'type')
print(m)
