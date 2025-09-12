import networkx as nx
import numpy as np

def google_matrix(G, alpha=0.85):
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G, nodelist=sorted(G.nodes()))
    out_degree = A.sum(axis=1)
    out_degree[out_degree == 0] = 1  # Avoid division by zero
    P = A / out_degree[:, None]

    dangling_nodes = (out_degree == 0)
    dangling_weight = 1.0 / n

    S = alpha * P + (1 - alpha) * np.ones((n, n)) / n
    
    for i in range(n):
        if dangling_nodes[i]:
            S[i, :] = dangling_weight

    return S

# Example usage
G = nx.DiGraph([(0, 1), (1, 2), (2, 0)])
G_matrix = google_matrix(G)
print(G_matrix)
