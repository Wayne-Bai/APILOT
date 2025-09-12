import networkx as nx
import numpy as np

def attribute_matrix(G, attributes=None):
    if attributes is None:
        # Return the adjacency matrix if no attributes are provided
        return nx.to_numpy_array(G)

    # Get attributes as a numpy array
    attr_matrix = np.array([list(nx.get_node_attributes(G, attr).values()) for attr in attributes]).T
    return attr_matrix

# Example usage:
# G = nx.Graph()
# G.add_node(1, label='A', value=3)
# G.add_node(2, label='B', value=5)
# G.add_edges_from([(1, 2)])
# attributes = ['label', 'value']
# print(attribute_matrix(G, attributes))
