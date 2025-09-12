import networkx as nx
import numpy as np

def return_google_matrix(graph, damping_factor=0.85, max_iterations=100, tolerance=1.0e-8):
    """
    This function returns the Google matrix of a graph.

    Parameters:
    - graph: Input graph
    - damping_factor: Damping factor (default is 0.85)
    - max_iterations: Maximum number of iterations (default is 100)
    - tolerance: Tolerance for convergence (default is 1.0e-8)

    Returns:
    - google_matrix: Google matrix of the input graph
    """
    
    # Check if the graph is directed
    if not graph.is_directed():
        raise ValueError('Google matrix is only defined for directed graphs')
    
    # Calculate the number of nodes in the graph
    num_nodes = graph.number_of_nodes()
    
    # Initialize the Google matrix
    google_matrix = np.zeros((num_nodes, num_nodes))
    
    # Initialize the base matrix for A
    base_matrix = np.ones((num_nodes, num_nodes)) / num_nodes
    
    # Iterate until max_iterations is reached
    for _ in range(max_iterations):
        # Perform matrix-vector multiplication
        prev_matrix = np.copy(google_matrix)
        google_matrix = np.dot(base_matrix, google_matrix) + np.eye(num_nodes)
        
        # Apply the damping factor
        google_matrix = (1 - damping_factor) / num_nodes + damping_factor * google_matrix
        
        # Check for convergence
        if np.linalg.norm(google_matrix - prev_matrix) < tolerance:
            break
    
    return google_matrix

# Example usage
G = nx.DiGraph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])
google_matrix = return_google_matrix(G)
print(google_matrix)
