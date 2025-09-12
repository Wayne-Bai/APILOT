import networkx as nx
import numpy as np

def attribute_matrix(G, attribute=None):
    if attribute is None:
        # If no attribute is specified, return the adjacency matrix
        return nx.to_numpy_array(G)
    else:
        # Get the attribute values for each node
        attributes = nx.get_node_attributes(G, attribute)
        # Create a matrix with the attribute values
        attribute_values = np.array([attributes[node] for node in G.nodes()])
        return attribute_values

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3)])
# G.nodes[1]['color'] = 'red'
# G.nodes[2]['color'] = 'blue'
# G.nodes[3]['color'] = 'green'
# print(attribute_matrix(G, 'color'))
