import networkx as nx
import numpy as np

def simrank(G, max_iter=100, C=0.8):
    n = len(G.nodes)
    sim = np.zeros((n, n))

    # Create a mapping from nodes to indices
    node_to_index = {node: idx for idx, node in enumerate(G.nodes)}

    # Initialize the diagonal elements to 1
    for node in G.nodes:
        sim[node_to_index[node], node_to_index[node]] = 1.0

    # Create adjacency matrix
    A = nx.adjacency_matrix(G).A

    # Calculate SimRank iteratively
    for _ in range(max_iter):
        new_sim = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                if i != j:
                    neighbors_i = np.nonzero(A[i])[0]
                    neighbors_j = np.nonzero(A[j])[0]
                    sim_sum = 0.0
                    
                    for ni in neighbors_i:
                        for nj in neighbors_j:
                            sim_sum += sim[ni, nj]
                    
                    if len(neighbors_i) > 0 and len(neighbors_j) > 0:
                        new_sim[i, j] = (C / (len(neighbors_i) * len(neighbors_j))) * sim_sum

        sim = new_sim

    # Invert the mapping to return the results in node format
    index_to_node = {idx: node for node, idx in node_to_index.items()}
    result = {index_to_node[i]: {index_to_node[j]: sim[i, j] for j in range(n)} for i in range(n)}

    return result

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
similarities = simrank(G)
print(similarities)
