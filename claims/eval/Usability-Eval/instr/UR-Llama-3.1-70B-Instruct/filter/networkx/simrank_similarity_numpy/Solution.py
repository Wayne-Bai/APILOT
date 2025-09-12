import networkx as nx
import numpy as np

def matrix_simrank(G, max_iter=100, tol=1e-8):
    n = len(G)
    A = nx.to_numpy_array(G)
    S = np.identity(n)
    
    for _ in range(max_iter):
        S_prev = S
        SS = np.dot(S, S.T)
        SA = np.dot(S, A)
        AS = np.dot(A, S)
        ASA = np.dot(AS, A.T)
        S_new = (0.8 * SA @ S.T @ A.T) + (0.6 * A @ SA) + (0.6 * AS @ A) + (0.2 * ASA @ S)
        S_new = (S_new / np.sum(S_new, axis=1, keepdims=True)).clip(min=0)
        S = (S_new + SS) / 2
        
        if np.linalg.norm(S - S_prev) < tol:
            break
    
    return S

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3)])

# Calculate SimRank matrix
simrank_matrix = matrix_simrank(G)

for i in range(len(simrank_matrix)):
    sorted_simranks = sorted(enumerate(simrank_matrix[i]), key=lambda x: x[1], reverse=True)
    print(f"SimRank for node {i+1}:")
    for node, rank in sorted_simranks:
        print(f"Node {node+1}: {rank:.4f}")
    print("\n")
