import networkx as nx
import numpy as np

def get_adjacency_matrix(graph):
    """
    Returns the adjacency matrix of the graph as a numpy matrix.

    Parameters:
    graph (nx.Graph): The input graph.

    Returns:
    np.matrix: The adjacency matrix of the graph.
    """
    # Get the number of nodes in the graph
    num_nodes = graph.number_of_nodes()
    
    # Initialize the adjacency matrix with zeros
    adj_matrix = np.zeros((num_nodes, num_nodes))
    
    # Iterate over all edges in the graph
    for u, v in graph.edges():
        # Set the corresponding entry in the adjacency matrix to 1
        adj_matrix[u, v] = 1
        adj_matrix[v, u] = 1
    
    return adj_matrix

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (3, 2)])
    
    # Get the adjacency matrix
    adj_matrix = get_adjacency_matrix(G)
    
    # Print the adjacency matrix
    print(adj_matrix)
