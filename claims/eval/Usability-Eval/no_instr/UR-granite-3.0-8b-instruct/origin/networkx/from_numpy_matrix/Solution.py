import networkx as nx
import numpy as np

def create_graph_from_numpy(numpy_matrix):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges based on the numpy matrix
    for i in range(numpy_matrix.shape[0]):
        for j in range(numpy_matrix.shape[1]):
            if numpy_matrix[i, j] == 1:
                G.add_edge(i, j)

    return G
