import networkx as nx
import numpy as np

def simrank(G, max_iter=100, c=0.8):
    """
    SimRank of nodes in G with matrix operations.

    Parameters
    ----------
    G : NetworkX graph
    max_iter : Maximum number of iterations
    c : Attenuation factor, ranges from 0 to 1

    Returns
    -------
    sim : dictionary with node pairs as keys, similarities as values
    """
    # Convert G to a matrix
    M = nx.to_numpy_matrix(G)

    # Get the indices of non-zero elements
    I = np.where(M > 0)

    # Get the indices of zero elements (which we need to process separately)
    I_zero = np.where(M == 0)

    # Get the shape of the matrix
    N = M.shape[0]

    # Initialize similarity matrix S
    S = np.eye(N)  # Identity matrix for now

    for _ in range(max_iter):
        # Compute new similarity matrix
        S_new = c * np.dot(np.dot(M, np.dot(S, M.T)), M.T)
        S_new[I_zero] = 0  # Reset similarity to 0 for zero elements
        S_new /= np.abs(S_new).sum(axis=1, keepdims=True)  # Normalize each row
        S = S_new

    # Compute SimRank scores
    sims = {}
    for u, v in G.nodes():
        sims[(u, v)] = S[u, v]

    return sims

# Create a sample graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 1), (1, 3), (3, 2), (2, 4), (4, 3)])

# Compute SimRank scores
sims = simrank(G)

# Print SimRank scores
for (u, v), sim in sims.items():
    print(f"SimRank({u}, {v}): {sim:.4f}")
