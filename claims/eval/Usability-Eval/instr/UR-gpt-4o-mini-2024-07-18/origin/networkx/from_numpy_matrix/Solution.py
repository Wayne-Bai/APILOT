import networkx as nx
import numpy as np

def graph_from_numpy_matrix(np_matrix):
    # Create a graph from the numpy adjacency matrix
    G = nx.from_numpy_array(np_matrix)
    return G

# Example usage
np_matrix = np.array([[0, 1, 0],
                      [1, 0, 1],
                      [0, 1, 0]])

graph = graph_from_numpy_matrix(np_matrix)

# Print the nodes and edges of the graph
print("Nodes:", graph.nodes())
print("Edges:", graph.edges())
