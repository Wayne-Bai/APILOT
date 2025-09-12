import networkx as nx
import numpy as np

def hits_hub_matrix(G, max_iter=100, tol=1.0e-8):
    """
    Returns the HITS hub matrix.

    Args:
    G (DiGraph): Input graph.
    max_iter (int): Maximum iterations.
    tol (float): Convergence tolerance.

    Returns:
    h (ndarray): HITS hub matrix.
    """
    W = nx.to_numpy_array(G, dtype=float)
    n = W.shape[0]
    h = np.ones(n)

    for _ in range(max_iter):
        h_new = W.T.dot(W).dot(h)
        h_norm = h_new / h_new.max()
        if np.allclose(h, h_norm, atol=tol):
            break
        h = h_norm

    return h

# Example usage:
if __name__ == "__main__":
    G = nx.DiGraph([(1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 2), (4, 2)])
    h = hits_hub_matrix(G)
    print("HITS Hub Matrix:", h)
