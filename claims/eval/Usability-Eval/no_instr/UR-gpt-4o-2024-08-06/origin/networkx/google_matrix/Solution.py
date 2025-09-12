import networkx as nx
import numpy as np

def google_matrix(G, alpha=0.85, personalization=None, nodelist=None):
    """Return the Google matrix of the graph."""
    n = len(G)
    if n == 0:
        return np.array([[]])

    # if nodelist is None, use G's nodes
    if nodelist is None:
        nodelist = list(G)

    # Create personalization vector if not provided
    if personalization is None:
        personalization = dict.fromkeys(G, 1.0 / n)
    else:
        # Make sure it's a stochastic vector
        s = float(sum(personalization.values()))
        personalization = {k: v / s for k, v in personalization.items()}

    # Create adjacency matrix
    A = nx.to_numpy_array(G, nodelist=nodelist)
    
    # Build the stochastic matrix M
    out_degree = A.sum(axis=1, keepdims=True)
    M = np.where(out_degree != 0, A / out_degree, 0.0)

    # Account for dangling nodes
    dangling_weights = personalization
    dangling_nodes = np.where(out_degree == 0)[0]

    # Create personalization matrix
    P = np.array([personalization.get(node, 0) for node in nodelist])

    # Calculate Google matrix
    G_matrix = alpha * M + (alpha * np.sum(M[:, dangling_nodes], axis=1)[:, np.newaxis] * P[np.newaxis, :]) + ((1 - alpha) * P[np.newaxis, :])
    
    return G_matrix

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])

google_matrix_G = google_matrix(G)
print(google_matrix_G)
