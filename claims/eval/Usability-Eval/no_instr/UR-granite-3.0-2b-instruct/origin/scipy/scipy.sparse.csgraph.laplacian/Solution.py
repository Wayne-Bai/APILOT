from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

def laplacian(graph):
    # Get the number of nodes
    n = graph.shape[0]

    # Initialize the Laplacian matrix
    L = csr_matrix(graph)

    # Set the diagonal elements to 0 (since the Laplacian of a graph is defined as L = D - A, where D is the degree matrix and A is the adjacency matrix)
    L.setdiag(L.diagonal())

    # Set the off-diagonal elements to -1 (since the Laplacian of a graph is defined as L = D - A)
    L.setdiag(L.diagonal(), k=-1)

    return L

# Example usage
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

L = laplacian(graph)
print(L.toarray())
