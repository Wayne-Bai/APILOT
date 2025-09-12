import networkx as nx
import numpy as np

def get_attribute_matrix(G, attribute=None):
    nodes = list(G.nodes())
    if attribute is None:
        # No attribute specified, construct the adjacency matrix
        matrix = nx.to_numpy_array(G, nodelist=nodes)
    else:
        # Attribute specified, construct the attribute matrix
        matrix = np.array([[G[u][v].get(attribute, 0) for v in nodes] for u in nodes])
    return matrix

# Create a graph
G = nx.Graph()
G.add_edge(1, 2, weight=0.5)
G.add_edge(2, 3, weight=1.0)

# Get the attribute matrix for the 'weight' attribute
weight_matrix = get_attribute_matrix(G, 'weight')
print("Weight Matrix:", weight_matrix)

# Get the adjacency matrix
adj_matrix = get_attribute_matrix(G)
print("Adjacency Matrix:", adj_matrix)
