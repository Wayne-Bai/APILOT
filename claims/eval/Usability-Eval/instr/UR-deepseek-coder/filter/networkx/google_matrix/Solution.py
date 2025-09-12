import networkx as nx
import numpy as np

def google_matrix(G, alpha=0.85):
    # Number of nodes in the graph
    n = G.number_of_nodes()
    
    # Initialize the Google matrix
    M = np.zeros((n, n))
    
    # Create the adjacency matrix
    A = nx.to_numpy_array(G)
    
    # Normalize the adjacency matrix by row sums
    row_sums = A.sum(axis=1)
    normalized_A = A / row_sums[:, np.newaxis]
    
    # Handle nodes with no outgoing edges (dangling nodes)
    dangling_nodes = np.where(row_sums == 0)[0]
    for node in dangling_nodes:
        normalized_A[node, :] = 1.0 / n
    
    # Construct the Google matrix
    M = alpha * normalized_A + (1 - alpha) / n * np.ones((n, n))
    
    return M

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(0, 1), (1, 2), (2, 0)])
# google_matrix_G = google_matrix(G)
# print(google_matrix_G)
