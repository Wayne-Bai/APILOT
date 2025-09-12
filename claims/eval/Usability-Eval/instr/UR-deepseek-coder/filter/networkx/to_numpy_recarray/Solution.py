import networkx as nx
import numpy as np

def graph_to_adjacency_matrix_recarray(G):
    # Get the adjacency matrix as a NumPy array
    adj_matrix = nx.to_numpy_array(G)
    
    # Convert the NumPy array to a structured array (recarray)
    dtype = [('weight', float)]
    recarray = np.rec.fromarrays([adj_matrix], dtype=dtype)
    
    return recarray

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])
adj_recarray = graph_to_adjacency_matrix_recarray(G)
print(adj_recarray)
