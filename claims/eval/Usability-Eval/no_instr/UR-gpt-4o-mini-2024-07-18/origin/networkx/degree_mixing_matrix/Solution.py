import networkx as nx
import numpy as np

def mixing_matrix(graph, attribute):
    # Get the unique values of the attribute
    unique_values = set(nx.get_node_attributes(graph, attribute).values())
    
    # Create a mapping from attribute values to indices
    value_to_index = {value: idx for idx, value in enumerate(unique_values)}
    
    # Create a zero matrix for the mixing matrix
    num_values = len(unique_values)
    mixing_matrix = np.zeros((num_values, num_values))
    
    # Populate the mixing matrix
    for node1, node2 in graph.edges():
        attr1 = nx.get_node_attributes(graph, attribute)[node1]
        attr2 = nx.get_node_attributes(graph, attribute)[node2]
        mixing_matrix[value_to_index[attr1], value_to_index[attr2]] += 1
    
    return mixing_matrix

# Example usage
# G = nx.Graph()
# G.add_node(1, color='red')
# G.add_node(2, color='blue')
# G.add_node(3, color='red')
# G.add_edges_from([(1, 2), (2, 3), (1, 3)])
# result = mixing_matrix(G, 'color')
# print(result)
