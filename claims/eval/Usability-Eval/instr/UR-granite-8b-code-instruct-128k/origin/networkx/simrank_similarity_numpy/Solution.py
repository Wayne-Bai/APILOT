import networkx as nx
import numpy as np

def simrank(G, alpha=0.85, threshold=1e-6):
    num_nodes = len(G)
    sim_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        sim_matrix[i, i] = 1.0
    for iter in range(100):
        next_sim_matrix = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    sim_ij = (alpha * sim_matrix[i, j]) + ((1 - alpha) * sum(sim_matrix[k, i] * sim_matrix[k, j] for k in range(num_nodes)))
                    next_sim_matrix[i, j] = sim_ij
        sim_matrix = next_sim_matrix
        if np.max(np.abs(sim_matrix - next_sim_matrix)) < threshold:
            break
    return sim_matrix
