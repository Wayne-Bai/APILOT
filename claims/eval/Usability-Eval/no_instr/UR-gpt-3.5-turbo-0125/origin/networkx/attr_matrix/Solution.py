
import numpy as np
import networkx as nx

def attribute_matrix(G):
    if nx.is_empty(G):
        return np.array([])

    attributes = list(G.nodes(data=True))[0][1].keys()  # Get the list of attribute keys
    node_list = list(G.nodes())
    
    num_nodes = len(node_list)
    num_attributes = len(attributes)
    
    attribute_array = np.zeros((num_nodes, num_attributes))

    for i, node in enumerate(node_list):
        for j, attr in enumerate(attributes):
            attribute_array[i][j] = G.nodes[node][attr]
    
    return attribute_array

# Example usage
G = nx.Graph()
G.add_node(1, color='red', weight=10)
G.add_node(2, color='blue', weight=20)
G.add_edge(1, 2)

attribute_matrix = attribute_matrix(G)
print(attribute_matrix)
