
import networkx as nx
import numpy as np

# Define function for calculating SimRank
def simrank(G, nodes):
    # Initialize matrices and variables
    A = nx.adjacency_matrix(G)
    D = np.diag(np.sum(A, axis=0))
    L = D - A
    T = np.transpose(L)
    N = len(nodes)

    # Calculate SimRank for each node
    simranks = []
    for i in range(N):
        # Calculate eigenvectors of the Laplacian matrix
        laplacian_eigs = np.linalg.eigvals(L)
        # Calculate SimRank value for current node
        simrank_value = (laplacian_eigs[0] + laplacian_eigs[1]) / 2
        simranks.append(simrank_value)
    return simranks

# Test the function
G = nx.DiGraph()
nodes = [0, 1, 2, 3, 4]
simranks = simrank(G, nodes)
print(simranks)
