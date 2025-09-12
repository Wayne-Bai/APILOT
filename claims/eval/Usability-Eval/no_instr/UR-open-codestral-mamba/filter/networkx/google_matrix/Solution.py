import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add edges with weights
edges = [("A", "B", 2), ("A", "C", 1), ("B", "C", 4), ("B", "D", 7), ("C", "D", 3)]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Calculate Google matrix
A = nx.to_numpy_array(G)
A = np.where(A==0, np.inf, A)
D = np.diag(np.sum(A, axis=1))
A = np.matmul(np.matmul(np.linalg.inv(D), A) , D)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i,j] *= 1/sum(A[:, j])

print(A)
