import networkx as nx
import numpy as np

def get_matrix(G, attr=None):
    """
    Returns the attribute matrix using attributes from G,
    If no attribute is passed then the adjacency matrix is constructed.
    """
    if attr is None:
        return nx.to_numpy_array(G)
    else:
        return nx.to_numpy_array(G, nodelist=G.nodes(), weight=attr, nonedge=0.0)

# Example usage:
G = nx.Graph()   # your graph here
G.add_edge(1, 2, weight=0.9)   # add some edges and attributes to the graph
matrix = get_matrix(G, 'weight')
print(matrix)
