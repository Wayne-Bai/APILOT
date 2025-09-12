import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix

def graph_from_sparse_matrix(sparse_matrix):
    # Ensure the input is a CSR sparse matrix
    if not isinstance(sparse_matrix, csr_matrix):
        raise ValueError("Input must be a scipy sparse csr_matrix")

    # Create a graph from the sparse matrix
    G = nx.from_scipy_sparse_matrix(sparse_matrix)

    return G

# Example usage
if __name__ == "__main__":
    # Create a sample sparse matrix
    data = np.array([1, 1, 1, 1])
    row_indices = np.array([0, 1, 2, 0])
    col_indices = np.array([1, 2, 0, 2])
    sparse_matrix = csr_matrix((data, (row_indices, col_indices)), shape=(3, 3))

    # Create the graph
    graph = graph_from_sparse_matrix(sparse_matrix)
    print(graph.edges())
