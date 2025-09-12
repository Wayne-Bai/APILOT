import scipy as sp
import numpy as np

def directed_laplacian(graph):
    """
    Return the Laplacian of a directed graph.

    Parameters
    ----------
    graph : scipy.sparse	matrix
        The adjacency matrix of the directed graph.

    Returns
    -------
    laplacian : scipy.sparse.matrix
        The Laplacian matrix of the directed graph.
    """

    # Calculate the degree of each node
    degrees = np.asarray(graph.sum(axis=1)).flatten()

    # Create a diagonal sparse matrix of the degrees
    diag_degrees = sp.sparse.diags(degrees)

    # Calculate the Laplacian matrix (degree matrix - adjacency matrix)
    laplacian = diag_degrees - graph

    return laplacian


# Example usage
if __name__ == "__main__":
    import scipy.sparse as sparse

    # Define the adjacency matrix of a directed graph
    adj_matrix = sparse.csr_matrix(np.array([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0]
    ]))

    # Calculate the Laplacian of the graph
    laplacian_matrix = directed_laplacian(adj_matrix)

    print(laplacian_matrix.toarray())
