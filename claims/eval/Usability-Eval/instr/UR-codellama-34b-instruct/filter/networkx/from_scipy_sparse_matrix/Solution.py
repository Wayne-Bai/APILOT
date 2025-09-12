import numpy as np
import networkx as nx
from scipy.sparse import lil_matrix

# Create a sparse matrix
A = lil_matrix((5, 5))
A[0, 1] = 2
A[1, 2] = 3
A[2, 3] = 4
A[3, 4] = 5

# Convert the sparse matrix to a NetworkX graph
G = nx.from_scipy_sparse_matrix(A)

# Print the edges of the graph
print("Edges:")
for u, v in G.edges():
    print((u, v))
