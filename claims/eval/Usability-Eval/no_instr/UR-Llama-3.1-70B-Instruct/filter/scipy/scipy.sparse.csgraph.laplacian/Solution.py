import scipy as sp
import numpy as np
from scipy import sparse

def laplacian_of_directed_graph(graph):
    """
    This function calculates the Laplacian of a directed graph.
    
    Parameters:
    graph (numpy array or scipy sparse matrix): The adjacency matrix of the graph.
    
    Returns:
    A (scipy sparse matrix): The Laplacian of the graph.
    """
    # Convert the graph to a scipy sparse matrix if it's not already one
    if not sparse.isspmatrix(graph):
        graph = sparse.csr_matrix(graph)
    
    # Calculate the out degree of each node
    out_degree = np.array(graph.sum(axis=1)).flatten()
    
    # Create a diagonal matrix of the out degrees
    out_degree_matrix = sparse.diags(out_degree)
    
    # Calculate the Laplacian
    laplacian = out_degree_matrix - graph
    
    return laplacian

# Example usage:
if __name__ == "__main__":
    # Create an example adjacency matrix
    adjacency_matrix = np.array([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
    ])

    # Calculate the Laplacian of the graph
    laplacian = laplacian_of_directed_graph(adjacency_matrix)
    
    print(laplacian.toarray())
