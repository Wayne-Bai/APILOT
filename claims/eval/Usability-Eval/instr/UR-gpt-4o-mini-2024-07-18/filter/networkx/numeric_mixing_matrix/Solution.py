import networkx as nx
import numpy as np

def mixing_matrix(graph, attribute):
    # Get unique attribute values
    attribute_values = set(nx.get_node_attributes(graph, attribute).values())
    
    # Create a mapping from attribute value to index
    attribute_index = {value: index for index, value in enumerate(attribute_values)}
    
    # Create an empty mixing matrix
    matrix = np.zeros((len(attribute_values), len(attribute_values)))
    
    # Fill the mixing matrix
    for u, v in graph.edges():
        attribute_u = nx.get_node_attributes(graph, attribute)[u]
        attribute_v = nx.get_node_attributes(graph, attribute)[v]
        
        if attribute_u in attribute_index and attribute_v in attribute_index:
            i = attribute_index[attribute_u]
            j = attribute_index[attribute_v]
            matrix[i][j] += 1
    
    return matrix

# Example usage:
# G = nx.Graph()
# G.add_node(1, group='A')
# G.add_node(2, group='B')
# G.add_node(3, group='A')
# G.add_edges_from([(1, 2), (1, 3), (2, 3)])
# result = mixing_matrix(G, 'group')
# print(result)
