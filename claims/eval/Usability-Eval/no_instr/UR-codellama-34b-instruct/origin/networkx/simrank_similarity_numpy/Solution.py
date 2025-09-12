import numpy as np
import networkx as nx

def simrank(G, alpha=0.8):
    """
    Calculates the SimRank similarity between all pairs of nodes in a graph G using matrices.
    
    Parameters
    ----------
    G : NetworkX graph
        The input graph.
    alpha : float, optional
        The damping factor. Default is 0.8.
    
    Returns
    -------
    simrank : dictionary of dictionaries
        A dictionary of dictionaries where the key is a node in G and the value is a dictionary with keys of other nodes in G and values of the SimRank similarity between the two nodes.
    """
    # Get the number of nodes in the graph
    n = len(G.nodes)
    
    # Initialize the matrix of shortest paths to infinity
    D = np.full((n, n), np.inf)
    
    # Initialize the diagonal entries of the matrix to 0
    for i in range(n):
        D[i, i] = 0
    
    # Fill in the matrix with the shortest paths between nodes
    for edge in G.edges:
        u, v = edge
        D[u, v] = min(D[u, v], 1)
        D[v, u] = min(D[v, u], 1)
    
    # Calculate the SimRank matrix using the matrix of shortest paths and the damping factor alpha
    S = np.linalg.inv(np.identity(n) - (alpha * D))
    
    # Initialize the dictionary of dictionaries to store the SimRanks
    simrank = {}
    
    # Loop over all pairs of nodes and calculate their SimRank similarity
    for i in range(n):
        for j in range(i+1, n):
            simrank[G.nodes[i], G.nodes[j]] = S[i, j]
    
    return simrank
