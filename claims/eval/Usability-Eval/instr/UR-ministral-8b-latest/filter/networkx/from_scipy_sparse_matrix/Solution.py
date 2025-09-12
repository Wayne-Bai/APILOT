import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix

# Function to convert scipy sparse matrix adjacency list to NetworkX graph
def sparse_matrix_to_networkx_graph(adjacency_data, row_data=None):
    if row_data is None:
        rows, cols = adjacency_data.indices, adjacency_data.indptr
    else:
        rows = adjacency_data.indices
        cols = row_data

    graph = nx.Graph()
    n_vertices = adjacency_data.shape[0]

    for row in range(rows):
        node1 = row
        for col in range(rows[row], rows[row + 1]):
            node2 = cols[col]
            graph.add_edge(node1, node2)

    return graph

# Example usage:
# Create a sparse adjacency matrix
adjacency = csr_matrix(
    [[0, 1, 0],
     [1, 0, 1],
     [0, 1, 0]], dtype=np.int
)

# Convert to a NetworkX graph
graph = sparse_matrix_to_networkx_graph(adjacency)
print(nx.adjacency_matrix(graph).toarray())
