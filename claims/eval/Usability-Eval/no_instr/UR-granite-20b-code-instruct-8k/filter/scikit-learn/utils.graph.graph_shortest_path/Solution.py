
import numpy as np
from scipy.sparse.csgraph import dijkstra

def shortest_path(graph, source, target):
    """
    Find the shortest path between a source node and a target node in a graph.

    Parameters:
    graph (array): adjacency matrix representing the graph
    source (int): index of the source node
    target (int): index of the target node

    Returns:
    path (list): list of nodes representing the shortest path
    distance (float): length of the shortest path
    """
    if graph.ndim != 2 or graph.shape[0] != graph.shape[1]:
        raise ValueError("Input graph must be a square matrix")
    if source < 0 or source >= graph.shape[0] or target < 0 or target >= graph.shape[0]:
        raise ValueError("Source and target indices are out of bounds")
    distances, predecessors = dijkstra(graph, source, return_predecessors=True)
    path = []
    node = target
    while node != source:
        path.append(node)
        node = predecessors[node]
    path.append(source)
    path = path[::-1]
    distance = distances[target]

    return path, distance
