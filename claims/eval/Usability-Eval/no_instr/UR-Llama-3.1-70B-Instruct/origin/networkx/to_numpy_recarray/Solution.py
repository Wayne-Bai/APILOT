import networkx as nx
import numpy as np

def get_adjacency_matrix(G):
    """
    Returns the graph adjacency matrix as a NumPy recarray.

    Parameters:
    G (networkx.Graph): Input graph.

    Returns:
    numpy.recarray: Adjacency matrix of the graph.
    """
    # Get the adjacency matrix
    adj_matrix = nx.to_numpy_array(G)
    
    # Convert the adjacency matrix to a NumPy recarray
    rec_array = np.recarray(adj_matrix.shape, dtype=[('weight', float)])
    rec_array.weight = adj_matrix
    
    return rec_array

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Get the adjacency matrix
adj_matrix = get_adjacency_matrix(G)

print(adj_matrix)
