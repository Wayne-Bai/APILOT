import networkx as nx
import numpy as np

def generate_adjacency_matrix(G):
    """
    This function returns the adjacency matrix of a given graph G.

    Args:
    G (nx.Graph): A networkx graph object

    Returns:
    np.ndarray: The adjacency matrix of the graph G
    """
    # Create an empty adjacency matrix filled with zeros.
    num_nodes = G.number_of_nodes()
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    # Populate the adjacency matrix with ones if there is an edge between two nodes.
    for edge in G.edges():
        u, v = edge
        adjacency_matrix[u, v] = 1
        adjacency_matrix[v, u] = 1  # Comment this line out if the graph is directed

    return adjacency_matrix


# Example usage:
if __name__ == "__main__":
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(1, 3)
    G.add_edge(3, 4)

    # Get the adjacency matrix
    adjacency_matrix = generate_adjacency_matrix(G)
    print(adjacency_matrix)
