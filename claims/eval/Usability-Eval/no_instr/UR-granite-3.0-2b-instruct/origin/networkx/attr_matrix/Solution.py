import networkx as nx
import numpy as np

def get_attribute_matrix(G, attribute_name):
    if attribute_name not in G.attributes():
        raise ValueError(f"Attribute '{attribute_name}' not found in graph")

    attribute_values = G.get_attribute(attribute_name)
    attribute_matrix = np.array(attribute_values).reshape(-1, 1)
    return attribute_matrix

# Example usage:
G = nx.Graph()
G.add_node(1, color='red', value=10)
G.add_node(2, color='blue', value=20)
G.add_edge(1, 2)

attribute_matrix = get_attribute_matrix(G, 'color')
print(attribute_matrix)
