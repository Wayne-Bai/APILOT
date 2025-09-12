import networkx as nx
import numpy as np

def simrank(G, alpha, max_iter):
    n = len(G.nodes)
    simrank_matrix = np.zeros((n, n))
    
    for i in range(n):
        simrank_matrix[i, i] = 1
    
    for _ in range(max_iter):
        new_simrank_matrix = np.zeros((n, n))
        for u in range(n):
            for v in range(n):
                simrank_u = simrank_matrix[u]
                simrank_v = simrank_matrix[v]
                similarity = sum(simrank_u[w] * simrank_v[w] for w in G.neighbors(u) & G.neighbors(v))
                new_simrank_matrix[u, v] = (1 - alpha) * similarity + alpha * simrank_matrix[u, v]
        simrank_matrix = new_simrank_matrix
    
    return simrank_matrix
