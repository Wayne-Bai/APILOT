import networkx as nx
import numpy as np

def calculate_simrank(G, alpha=0.5, epsilon=1e-6):
    n = len(G.nodes())
    simrank_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            simrank_matrix[i][j] = calculate_simrank_pair(G, i, j, alpha, epsilon)

    return simrank_matrix

def calculate_simrank_pair(G, i, j, alpha, epsilon):
    if i == j:
        return 1.0

    common_neighbors = list(set(G.neighbors(i)) & set(G.neighbors(j)))
    simrank_ij = 0.0

    for k in common_neighbors:
        simrank_ij += alpha * calculate_simrank_pair(G, i, k, alpha, epsilon) * calculate_simrank_pair(G, k, j, alpha, epsilon)

    simrank_ij = (1 - alpha) + alpha * simrank_ij

    if simrank_ij < epsilon:
        simrank_ij = 0.0

    return simrank_ij
