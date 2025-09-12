import networkx as nx
import numpy as np

def calculate_simrank(G):
    # Estimate the number of edges and nodes in the graph
    n = len(G)

    # Create a matrix to store the weights of nodes
    weights = np.zeros((n, n), dtype=float)

    # Initialize the base weight for self-loops
    for i in range(n):
        weights[i, i] = 1.0

    # Calculate the similarity matrix
    for i in range(n):
        weights[i, i] = 1.0
        for j in range(i+1, n):
            try:
                # Check if there are paths between node i and j
                path = nx.all_shortest_paths(G, source=i, target=j, weight='weight')
                if len(path) > 0:
                    shortest_path_weight = sum([path[-1][weight] for path in range(len(path)-1)]) / (len(path) - 1)
                    weights[i, j] = 1.0 / weights[j, j] if weights[j, j] > 0 else 0.0
                    weights[i, j] = weights[i, i] * (shortest_path_weight + 1.0 / weights[j, j])
            except nx.NetworkXNoPath:
                continue

    # Update the matrix until convergence
    while True:
        previous_weights = weights.copy()
        for i in range(n):
            for j in range(n):
                weights[i, j] = 0.0
                for k in range(n):
                    if i != k and j != k:
                        weights[i, j] += weights[i, k] * weights[k, j]
        if np.all(np.isclose(previous_weights, weights)):
            break

    return weights

# Example usage
G = nx.erdos_renyi_graph(10, 0.3)
simrank_matrix = calculate_simrank(G)
print(simrank_matrix)
