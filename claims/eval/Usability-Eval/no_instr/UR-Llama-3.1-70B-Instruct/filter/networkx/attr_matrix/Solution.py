import networkx as nx
import numpy as np

def get_attribute_matrix(G, attr=None):
    """
    Returns the attribute matrix using attributes from G as a numpy array.
    If only G is passed in, then the adjacency matrix is constructed.

    Parameters:
    G (networkx.Graph): input graph.
    attr (string, optional): attribute name.

    Returns:
    numpy.ndarray: attribute matrix.
    """
    if attr is None:
        # Construct adjacency matrix if attr is not provided
        return nx.to_numpy_array(G)
    else:
        # Get attribute matrix
        return nx.attribute_to_numpy_array(G, attr)

# Example usage:
# Create an example graph with node attributes
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])
nx.set_node_attributes(G, {1: 0.5, 2: 0.3, 3: 0.2}, name='weight')

# Get adjacency matrix
adj_matrix = get_attribute_matrix(G)
print("Adjacency Matrix:")
print(adj_matrix)

# Get attribute matrix for 'weight'
weight_matrix = get_attribute_matrix(G, 'weight')
print("\nWeight Matrix:")
print(weight_matrix)
