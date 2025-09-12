import networkx as nx
import numpy as np

# define the graph G
G = nx.gnp_random_graph(10, 0.5)

# calculate SimRank of nodes in G using matrices with NumPy
def simrank(G):
    A = nx.adjacency_matrix(G).todense()
    W = np.ones((len(A), len(A))) * (1 - 0.5)
    S = np.eye(len(A)) + 0.5 * A
    B = S.T @ (S @ W)
    C = np.linalg.inv(B)
    sim_matrix = C @ A.T
    return sim_matrix

# print the SimRank matrix for all nodes in G
print(simrank(G))
