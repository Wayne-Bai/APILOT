import networkx as nx
import numpy as np

def attribute_matrix(G, attribute=None):
    # If no attribute is specified, return the adjacency matrix
    if attribute is None:
        return nx.to_numpy_array(G)
    
    # Get the number of nodes
    num_nodes = G.number_of_nodes()
    
    # Initialize the attribute matrix
    attr_matrix = np.zeros((num_nodes, num_nodes))
    
    # Fill the attribute matrix
    for i, (u, v) in enumerate(G.edges()):
        if attribute in G[u][v]:
            attr_matrix[u][v] = G[u][v][attribute]
            attr_matrix[v][u] = G[u][v][attribute]  # Assuming undirected graph
    
    return attr_matrix
