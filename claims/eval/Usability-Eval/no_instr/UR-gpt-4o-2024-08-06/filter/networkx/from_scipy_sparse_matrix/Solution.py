import networkx as nx
from scipy.sparse import csr_matrix

def create_graph_from_sparse_matrix(sparse_matrix):
    # Ensure the input is a CSR sparse matrix
    if not isinstance(sparse_matrix, csr_matrix):
        raise TypeError("The input must be a scipy.sparse.csr_matrix.")

    # Create a graph from the adjacency matrix
    graph = nx.from_scipy_sparse_matrix(sparse_matrix)
    
    return graph

# Example usage
sparse_matrix = csr_matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
graph = create_graph_from_sparse_matrix(sparse_matrix)

# Output the graph information
print(nx.info(graph))
