import networkx as nx
import numpy as np

# Assuming G is your networkx graph
n = len(G)
sim_matrix = np.zeros((n, n))
sim_matrix.fill(1)  # initializing the matrix with 1s

def simrank(G, sim_matrix, iterations=10):
    for _ in range(iterations):
        sim_matrix_prev = sim_matrix.copy()
        for u, v in G.edges():
            for k, l in G.edges():
                sim_matrix[u, l] = (sim_matrix_prev[u, k] + sim_matrix_prev[v, l]) / 2
    return sim_matrix

sim_matrix = simrank(G, sim_matrix)
