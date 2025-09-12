
import networkx as nx
import numpy as np

# Define a function to generate the attribute matrix
def attribute_matrix(G):  
    if not nx.get_edge_attributes(G):  
        return nx.adjacency_matrix(G).toarray()
    
    attributes = list(nx.get_node_attributes(G, 'attribute').values())
    attr_matrix = np.array(attributes)
    
    return attr_matrix

# Example usage:
G = nx.Graph()
G.add_edge(1, 2, attribute='weight1')
G.add_node(1, attribute='color1')
G.add_node(2, attribute='color2')

attr_matrix = attribute_matrix(G)
print(attr_matrix)
