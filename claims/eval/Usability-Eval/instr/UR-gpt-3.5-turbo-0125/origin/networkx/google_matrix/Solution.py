
import numpy as np
import networkx as nx

def calculate_google_matrix(graph):
    n = len(graph)
    out_degrees = dict(graph.out_degree())
    matrix = np.zeros((n, n))

    for u, v in graph.edges():
        matrix[v][u] = 1 / out_degrees[u]

    return matrix

# Example
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])
google_matrix = calculate_google_matrix(G)
print(google_matrix)
