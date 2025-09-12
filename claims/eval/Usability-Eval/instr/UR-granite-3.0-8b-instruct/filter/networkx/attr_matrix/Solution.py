import networkx as nx
import numpy as np

def get_attribute_matrix(G):
    # Get the node attributes
    node_attrs = nx.get_node_attributes(G, 'attr')

    # Create a numpy array to store the attribute matrix
    attr_matrix = np.zeros((len(G.nodes), len(node_attrs[next(iter(node_attrs))])))

    # Fill the attribute matrix
    for i, node in enumerate(G.nodes):
        attr_matrix[i] = [node_attrs[node][attr] for attr in node_attrs[node]]

    return attr_matrix
