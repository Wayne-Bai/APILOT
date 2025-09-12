import networkx as nx
import numpy as np

def get_attribute_matrix(G):
    # Check if the graph has attributes
    if not nx.get_node_attributes(G, 'attribute_name'):
        raise ValueError("Graph does not have the specified attribute.")

    # Get the attribute values for each node
    attribute_values = nx.get_node_attributes(G, 'attribute_name').values()

    # Create a numpy array from the attribute values
    attribute_matrix = np.array(attribute_values)

    return attribute_matrix
