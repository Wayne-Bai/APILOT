import networkx as nx
import numpy as np

def google_matrix(graph, alpha=0.85):
    """
    Returns the Google matrix of the given graph.

    Parameters:
    graph (networkx.Graph): The input graph.
    alpha (float): Damping factor, typically between 0 and 1.

    Returns:
    np.ndarray: The Google matrix of the graph.
    """
    # Convert the graph to a directed graph if it is not
    if not nx.is_directed(graph):
        graph = graph.to_directed()

    # Number of nodes
    n = graph.number_of_nodes()
    
    # Create adjacency matrix
    adj_matrix = nx.to_numpy_array(graph, nodelist=sorted(graph.nodes()))
    
    # Replace zeros with small epsilon to avoid division by zero
    eps = 1e-10
    adj_matrix = np.where(adj_matrix == 0, eps, adj_matrix)

    # Normalize the adjacency matrix to create the stochastic matrix
    row_sums = adj_matrix.sum(axis=1, keepdims=True)
    stochastic_matrix = adj_matrix / row_sums

    # Create the Google matrix: G = alpha * P + (1 - alpha) * (1/n) * J
    # where P is the stochastic matrix, J is the all-ones matrix
    google_matrix = alpha * stochastic_matrix + (1 - alpha) * (1/n) * np.ones((n, n))

    return google_matrix
