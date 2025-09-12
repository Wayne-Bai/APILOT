import networkx as nx
import scipy.sparse as sp

def graph_to_sparse_matrix(graph):
    # Convert the graph to an adjacency matrix
    adjacency_matrix = nx.to_numpy_array(graph)
    
    # Convert the adjacency matrix to a SciPy sparse matrix
    sparse_matrix = sp.csr_matrix(adjacency_matrix)
    
    return sparse_matrix

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(0, 1), (1, 2), (2, 0)])
# sparse_adj_matrix = graph_to_sparse_matrix(G)
