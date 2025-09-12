import networkx as nx
import numpy as np

def compute_google_matrix(graph, alpha=0.85):
    A = nx.adjacency_matrix(graph).todense()
    N = A.shape[0]
    
    # Create a stochastic matrix
    D = np.array(A.sum(axis=1)).flatten()
    stochastic_matrix = A / D[:, np.newaxis]  # Broadcasting to make each row sum to 1
    
    # Handle dangling nodes (rows that sum to 0)
    for i in range(N):
        if D[i] == 0:
            stochastic_matrix[i] = np.ones(N) / N  # Assign uniform distribution to dangling nodes
    
    # Create the Google matrix
    google_matrix = alpha * stochastic_matrix + (1 - alpha) * np.ones((N, N)) / N
    
    return google_matrix

# Example usage
G = nx.erdos_renyi_graph(5, 0.5)  # Create a random graph
google_matrix = compute_google_matrix(G)
print(google_matrix)
