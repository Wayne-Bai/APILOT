import networkx as nx
import numpy as np

def google_matrix(G, alpha=0.85):
    """
    Returns the Google matrix of the graph G.

    Parameters:
    G (networkx.Graph): The input graph.
    alpha (float): The damping factor, default is 0.85.

    Returns:
    numpy.ndarray: The Google matrix of the graph.
    """
    # Number of nodes in the graph
    N = G.number_of_nodes()
    
    # Initialize the Google matrix with zeros
    M = np.zeros((N, N))
    
    # Create a dictionary to map node labels to indices
    node_to_index = {node: idx for idx, node in enumerate(G.nodes())}
    
    # Fill the Google matrix
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if len(neighbors) == 0:
            # If the node has no outgoing edges, distribute its weight uniformly
            M[node_to_index[node], :] = 1.0 / N
        else:
            # Distribute the node's weight to its neighbors
            for neighbor in neighbors:
                M[node_to_index[node], node_to_index[neighbor]] = 1.0 / len(neighbors)
    
    # Apply the damping factor
    M = alpha * M + (1 - alpha) / N * np.ones((N, N))
    
    return M

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# google_matrix(G)
