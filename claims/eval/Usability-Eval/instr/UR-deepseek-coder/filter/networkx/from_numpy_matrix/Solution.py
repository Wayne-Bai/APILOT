import networkx as nx
import numpy as np

def graph_from_numpy_matrix(matrix):
    G = nx.Graph()
    rows, cols = np.where(matrix != 0)
    edges = zip(rows.tolist(), cols.tolist())
    G.add_edges_from(edges)
    return G

# Example usage:
# matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
# G = graph_from_numpy_matrix(matrix)
# print(G.edges())
