import networkx as nx
import numpy as np

def attribute_matrix(G, attribute=None):
    if attribute is None:
        return nx.to_numpy_array(G)
    else:
        attr_values = nx.get_node_attributes(G, attribute)
        nodes = G.nodes()
        matrix = np.array([attr_values[node] if node in attr_values else 0 for node in nodes])
        return np.diag(matrix)
