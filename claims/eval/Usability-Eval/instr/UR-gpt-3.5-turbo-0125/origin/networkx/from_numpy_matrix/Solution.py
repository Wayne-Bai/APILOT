
import networkx as nx
import numpy as np

def graph_from_numpy_matrix(matrix):
    G = nx.from_numpy_matrix(np.matrix(matrix))
    return G

# Example usage
numpy_matrix = [[0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]]

graph = graph_from_numpy_matrix(numpy_matrix)
print("Nodes of the graph:", graph.nodes())
print("Edges of the graph:", graph.edges())
