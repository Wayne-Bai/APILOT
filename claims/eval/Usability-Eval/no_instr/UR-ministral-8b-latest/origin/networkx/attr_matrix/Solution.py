import networkx as nx
import numpy as np

def get_attribute_matrix(G):
    if G.number_of_attributes() == 0:
        return nx.to_numpy_array(G)
    else:
        return np.array([list(G.nodes[node].get(attr, 0)) for node in G.nodes for attr in G.nodes[node]]).T

# Example usage
G = nx.Graph()
G.add_edge(1, 2, weight=0.5)
G.add_node(3, color="red")
G.add_node(4, weight=1.2, size=2)

attribute_matrix = get_attribute_matrix(G)
print(attribute_matrix)
