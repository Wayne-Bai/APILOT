import networkx as nx
import numpy as np

def graph_to_adjacency_recarray(graph):
    # Get the adjacency matrix as a NumPy array
    adjacency_matrix_array = nx.to_numpy_array(graph)
    
    # Convert to a structured array (recarray)
    dtype = [('node_' + str(i), float) for i in range(adjacency_matrix_array.shape[1])]
    adjacency_recarray = np.core.records.fromarrays(adjacency_matrix_array.T, dtype=dtype)
    
    return adjacency_recarray

# Example usage
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3)])
adjacency_recarray = graph_to_adjacency_recarray(G)
print(adjacency_recarray)
