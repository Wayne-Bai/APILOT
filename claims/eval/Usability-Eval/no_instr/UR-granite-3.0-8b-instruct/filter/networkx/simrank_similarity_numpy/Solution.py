import networkx as nx
import numpy as np

def simrank(G, alpha=0.5, max_iter=100, tol=1e-6):
    n = len(G.nodes())
    sim_matrix = np.zeros((n, n))
    prev_sim_matrix = np.zeros((n, n))

    for iter_ in range(max_iter):
        prev_sim_matrix = sim_matrix.copy()
        for i in range(n):
            for j in range(n):
                sim_matrix[i, j] = sum(prev_sim_matrix[i, k] * prev_sim_matrix[k, j] for k in range(n)) / (len(G.neighbors(i)) * len(G.neighbors(j)))
                sim_matrix[i, j] = alpha * sim_matrix[i, j] + (1 - alpha) * np.mean(sim_matrix)

        if np.linalg.norm(sim_matrix - prev_sim_matrix) < tol:
            break

    return sim_matrix

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
sim_matrix = simrank(G)
print(sim_matrix)
