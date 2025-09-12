import networkx as nx
import numpy as np

def numpy_matrix_to_graph(matrix):
    """
    Return a graph from numpy matrix.
    
    The numpy matrix is interpreted as an adjacency matrix for the graph.
    
    Parameters:
    matrix (numpy.ndarray): Adjacency matrix representing the graph
    
    Returns:
    nx.Graph: A networkx graph object
    """
    # Ensure the matrix is symmetric (i.e., it represents an undirected graph)
    matrix = np.atleast_2d(matrix)
    if not np.allclose(matrix, matrix.T):
        raise ValueError("Matrix is not symmetric")
    
    # Create a new empty graph
    G = nx.Graph()
    
    # Add nodes to the graph
    num_nodes = matrix.shape[0]
    G.add_nodes_from(range(num_nodes))
    
    # Add edges to the graph
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if matrix[i, j] > 0:
                G.add_edge(i, j, weight=matrix[i, j])
    
    return G

# Example usage
matrix = np.array([[0, 1, 1, 0],
                   [1, 0, 1, 1],
                   [1, 1, 0, 1],
                   [0, 1, 1, 0]])

G = numpy_matrix_to_graph(matrix)
nx.draw(G, with_labels=True)
