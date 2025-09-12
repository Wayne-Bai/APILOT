import networkx as nx
import numpy as np

def adjacency_matrix(graph):
    """Return adjacency matrix of graph as a numpy matrix."""
    return nx.to_numpy_matrix(graph)
