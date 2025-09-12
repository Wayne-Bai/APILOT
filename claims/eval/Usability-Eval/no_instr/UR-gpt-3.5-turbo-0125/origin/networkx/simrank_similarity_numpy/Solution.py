
import numpy as np

def calculate_simrank(G, C=0.8, max_iter=100, eps=1e-4):
    nodes = list(G.nodes())
    num_nodes = len(nodes)
    sim_matrix = np.identity(num_nodes)  # Initialize similarity matrix with identity matrix

    for _ in range(max_iter):
        prev_sim_matrix = np.copy(sim_matrix)
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i == j:
                    continue

                sim_value = 0
                in_neighbors_i = list(G.predecessors(nodes[i]))
                in_neighbors_j = list(G.predecessors(nodes[j]))

                if len(in_neighbors_i) == 0 or len(in_neighbors_j) == 0:
                    sim_matrix[i][j] = 0
                    continue

                for in_neighbor_i in in_neighbors_i:
                    for in_neighbor_j in in_neighbors_j:
                        sim_value += prev_sim_matrix[nodes.index(in_neighbor_i)][nodes.index(in_neighbor_j)]

                sim_matrix[i][j] = (C / (len(in_neighbors_i) * len(in_neighbors_j))) * sim_value

        if np.allclose(sim_matrix, prev_sim_matrix, atol=eps):
            break

    return sim_matrix
