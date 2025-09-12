import networkx as nx
import numpy as np

def compute_hub_matrix(graph):
    # Compute HITS algorithm to get hubs and authorities scores
    hubs, authorities = nx.hits(graph, normalized=True)

    # Number of nodes
    num_nodes = len(graph.nodes)

    # Create a zero matrix for hub matrix
    hub_matrix = np.zeros((num_nodes, num_nodes))

    # Populate the hub matrix
    for i, (node_i, hub_score_i) in enumerate(hubs.items()):
        for j, (node_j, hub_score_j) in enumerate(hubs.items()):
            hub_matrix[i, j] = hub_score_i if node_i == node_j else 0

    return hub_matrix

# Example of usage
G = nx.DiGraph()
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 1)]
G.add_edges_from(edges)

hub_matrix = compute_hub_matrix(G)
print("HITS Hub Matrix:")
print(hub_matrix)
