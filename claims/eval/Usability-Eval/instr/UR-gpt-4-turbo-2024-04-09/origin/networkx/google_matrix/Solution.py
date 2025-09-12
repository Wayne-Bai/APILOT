import networkx as nx
import numpy as np

def google_matrix(G, alpha=0.85):
    # Create a stochastic adjacency matrix
    n = len(G)
    M = nx.to_numpy_array(G)
    out_degree = M.sum(axis=1)
    for i in range(n):
        for j in range(n):
            M[j, i] = M[j, i] / out_degree[i] if out_degree[i] > 0 else 0

    # Apply the damping factor
    S = np.ones((n, n)) / n
    G_matrix = alpha * M + (1 - alpha) * S

    return G_matrix

# Example usage:
G = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 2)])
G_matrix = google_matrix(G)
print(G_matrix)
