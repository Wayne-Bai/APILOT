import networkx as nx
import numpy as np

def create_graph_from_numpy_matrix(matrix):
    G = nx.from_numpy_array(matrix)
    return G

# Example usage
adj_matrix = np.array([[0, 1, 1],
                       [1, 0, 0],
                       [1, 0, 0]])
graph = create_graph_from_numpy_matrix(adj_matrix)
print(nx.info(graph))
