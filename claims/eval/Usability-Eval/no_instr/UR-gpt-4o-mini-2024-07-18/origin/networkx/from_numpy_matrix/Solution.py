import networkx as nx
import numpy as np

def adjacency_matrix_to_graph(adj_matrix):
    # Create a graph from the adjacency matrix
    graph = nx.from_numpy_matrix(adj_matrix)
    return graph

# Example usage
adj_matrix = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]])

graph = adjacency_matrix_to_graph(adj_matrix)
print(graph.nodes)  # Prints the nodes of the graph
print(graph.edges)  # Prints the edges of the graph
