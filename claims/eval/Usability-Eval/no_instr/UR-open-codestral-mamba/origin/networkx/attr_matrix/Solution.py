import networkx as nx
import numpy as np

# Assuming G is the graph

def get_attribute_matrix(G, attribute=None):
    if attribute is None:
        # If no attribute is specified, we create an adjacency matrix
        return nx.adjacency_matrix(G).todense()
    else:
        # Create a dictionary to store the attribute values
        attrs = nx.get_node_attributes(G, attribute)

        # Create a numpy array with the attribute values
        attr_array = np.array(list(attrs.values()))

        return attr_array

# Test the function with a simple graph
G = nx.Graph()
G.add_node(1, attr1=10, attr2=20)
G.add_node(2, attr1=30, attr2=40)
G.add_edge(1, 2)

# Print the adjacency matrix
print("Adjacency Matrix:")
print(get_attribute_matrix(G))

# Print the attribute matrix with attribute 'attr1'
print("Attribute Matrix with attr1:")
print(get_attribute_matrix(G, 'attr1'))
