import networkx as nx
import numpy as np

def attribute_matrix(G, attributes=None):
    if attributes is None:
        # If no attributes are provided, return the adjacency matrix
        return nx.to_numpy_array(G)
    else:
        # Create the attribute matrix using the specified attributes
        attr_data = [G.nodes[node].get(attr, 0) for node in G.nodes for attr in attributes]
        attr_matrix = np.array(attr_data).reshape(len(G.nodes()), -1)
        return attr_matrix
