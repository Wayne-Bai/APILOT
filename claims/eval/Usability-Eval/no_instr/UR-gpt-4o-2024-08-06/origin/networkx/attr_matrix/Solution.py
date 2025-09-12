import networkx as nx
import numpy as np

def get_attribute_matrix(G, node_attributes=None):
    if node_attributes is None:
        # If no node attributes are given, return the adjacency matrix
        return nx.adjacency_matrix(G).toarray()
    else:
        # For generating attribute matrix using specified node attributes
        nodes = list(G.nodes())
        node_count = len(nodes)
        
        # Create an empty matrix to store node attributes
        attribute_count = len(node_attributes)
        attribute_matrix = np.zeros((node_count, attribute_count))
        
        for i, node in enumerate(nodes):
            for j, attr in enumerate(node_attributes):
                attribute_matrix[i, j] = G.nodes[node].get(attr, 0)
        
        return attribute_matrix

# Example usage:
G = nx.Graph()
G.add_nodes_from([
    (1, {'attr1': 0.1, 'attr2': 0.3}),
    (2, {'attr1': 0.2, 'attr2': 0.2}),
    (3, {'attr1': 0.4, 'attr2': 0.1}),
])
# Retrieve adjacency matrix
adjacency_matrix = get_attribute_matrix(G)
print("Adjacency Matrix:\n", adjacency_matrix)

# Retrieve attribute matrix for specified attributes
node_attributes = ['attr1', 'attr2']
attribute_matrix = get_attribute_matrix(G, node_attributes)
print("Attribute Matrix:\n", attribute_matrix)
