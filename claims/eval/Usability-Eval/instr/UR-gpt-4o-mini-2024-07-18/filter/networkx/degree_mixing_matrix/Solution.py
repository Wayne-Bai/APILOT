import networkx as nx
import numpy as np

def mixing_matrix(G, attribute):
    # Get the unique values of the attribute
    unique_values = set(nx.get_node_attributes(G, attribute).values())
    
    # Create a mapping from attribute values to indices
    value_to_index = {value: i for i, value in enumerate(unique_values)}
    
    # Initialize the mixing matrix
    mix_matrix = np.zeros((len(unique_values), len(unique_values)))
    
    # Populate the mixing matrix
    for u, v in G.edges():
        attr_u = G.nodes[u][attribute]
        attr_v = G.nodes[v][attribute]
        index_u = value_to_index[attr_u]
        index_v = value_to_index[attr_v]
        mix_matrix[index_u, index_v] += 1
    
    return mix_matrix

# Example of usage:
# G = nx.Graph()
# G.add_node(1, attr='A')
# G.add_node(2, attr='B')
# G.add_node(3, attr='A')
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# mixing_mat = mixing_matrix(G, 'attr')
# print(mixing_mat)
