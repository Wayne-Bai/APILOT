import networkx as nx
import numpy as np

def google_matrix(G, alpha=0.85):
    """
    Returns the Google matrix of the graph.

    Parameters:
    G (DiGraph): directed graph
    alpha (float): parameter for PageRank, default=0.85

    Returns:
    numpy array: Google matrix of the graph
    """
    n = G.number_of_nodes()
    google_matrix = np.zeros((n, n))

    for i in range(n):
        out_edges = list(G.out_edges(i))
        if out_edges:
            for j, _ in out_edges:
                google_matrix[i, j] = 1 / len(out_edges)

    for i in range(n):
        in_edges = list(G.in_edges(i))
        if not in_edges:
            google_matrix[:, i] = 1 / n

    google_matrix = alpha * google_matrix + (1 - alpha) / n

    return google_matrix

# Example usage
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 0), (0, 2), (2, 0), (1, 2)])

google_matrix_G = google_matrix(G)
print(google_matrix_G)
