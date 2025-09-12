import networkx as nx
import numpy as np

def calculate_simrank(G):
    # Convert the graph to an adjacency matrix using NetworkX's modern API
    adj_matrix = nx.adjacency_matrix(G).todense()

    # Initialize the similarity matrix
    sim_matrix = np.eye(adj_matrix.shape[0])

    # Set up the parameters
    tau = 0.85
    beta = 2
    max_iter = 100
    epsilon = 1e-6

    # Start the SimRank algorithm
    for _ in range(max_iter):
        # Compute the new similarity matrix
        new_sim_matrix = (tau * np.dot(adj_matrix, sim_matrix) * adj_matrix.T +
                         (1 - tau) * np.eye(adj_matrix.shape[0]))

        # Check convergence
        if np.linalg.norm(new_sim_matrix - sim_matrix) < epsilon:
            break

        # Update the similarity matrix
        sim_matrix = new_sim_matrix

    return sim_matrix

# Example usage (you need to define a graph 'G' using networkx):
# G = nx.erdos_renyi_graph(100, 0.1)
# sim_rank = calculate_simrank(G)
# print(sim_rank)
