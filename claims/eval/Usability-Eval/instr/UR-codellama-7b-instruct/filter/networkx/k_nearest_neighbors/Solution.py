
from networkx import Graph
import numpy as np

def compute_average_degree_connectivity(graph, k=2):
    # Compute the degree connectivity for each node in the graph
    degrees = np.zeros(len(graph))
    for i in range(len(graph)):
        neighbors = graph.neighbors(i)
        for j in range(len(neighbors)):
            if neighbors[j] < k:
                degrees[i] += 1
    # Compute the average degree connectivity
    return np.mean(degrees)
