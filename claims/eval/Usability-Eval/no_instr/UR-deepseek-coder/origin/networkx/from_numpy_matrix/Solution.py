import networkx as nx
import numpy as np

def graph_from_numpy_matrix(adj_matrix):
    # Create an empty graph
    G = nx.Graph()
    
    # Get the number of nodes from the matrix size
    num_nodes = adj_matrix.shape[0]
    
    # Add nodes to the graph
    G.add_nodes_from(range(num_nodes))
    
    # Add edges based on the adjacency matrix
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adj_matrix[i, j] != 0:
                G.add_edge(i, j, weight=adj_matrix[i, j])
    
    return G

# Example usage:
adj_matrix = np.array([[0, 1, 0], [1, 0, 2], [0, 2, 0]])
G = graph_from_numpy_matrix(adj_matrix)
print(G.edges(data=True))
