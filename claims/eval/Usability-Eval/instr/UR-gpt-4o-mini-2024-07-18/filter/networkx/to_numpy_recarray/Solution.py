import networkx as nx
import numpy as np

def adjacency_matrix_to_recarray(graph):
    # Get the adjacency matrix as a NumPy array
    adj_matrix = nx.to_numpy_array(graph)
    
    # Create a structured numpy recarray
    recarray = np.core.records.fromarrays(adj_matrix.T, 
                                          names=','.join(['node_{}'.format(i) for i in range(adj_matrix.shape[1])]))
    
    return recarray

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])
recarray = adjacency_matrix_to_recarray(G)
print(recarray)
