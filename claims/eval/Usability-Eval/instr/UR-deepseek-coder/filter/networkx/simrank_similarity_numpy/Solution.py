import networkx as nx
import numpy as np

def simrank(G, c=0.8, max_iter=100, tol=1e-4):
    # Initialize SimRank matrix
    nodes = list(G.nodes())
    n = len(nodes)
    S = np.eye(n)  # S[i, j] is the SimRank score between nodes i and j

    for _ in range(max_iter):
        new_S = np.eye(n)
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nodes[i], nodes[j]
                    if len(list(G.neighbors(a))) == 0 or len(list(G.neighbors(b))) == 0:
                        new_S[i, j] = 0
                    else:
                        sim_sum = sum(S[nodes.index(a_prime), nodes.index(b_prime)] for a_prime in G.neighbors(a) for b_prime in G.neighbors(b))
                        new_S[i, j] = (c * sim_sum) / (len(list(G.neighbors(a))) * len(list(G.neighbors(b))))
        if np.allclose(S, new_S, atol=tol):
            break
        S = new_S

    return S

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
simrank_matrix = simrank(G)
print(simrank_matrix)
