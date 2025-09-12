import networkx as nx
import numpy as np

def get_adjacency_matrix(graph):
    """
    Returns adjacency matrix of G.

    Parameters:
    graph (nx.Graph): Input graph

    Returns:
    np.ndarray: Adjacency matrix of G
    """
    return nx.to_numpy_array(graph)

# Example usage
if __name__ == "__main__":
    # Create an empty graph
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from([1, 2, 3, 4])

    # Add edges
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 2), (3, 4), (4, 1)])

    # Get adjacency matrix
    adjacency_matrix = get_adjacency_matrix(G)

    # Print adjacency matrix
    print(adjacency_matrix)
