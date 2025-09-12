import networkx as nx
import numpy as np

def mixing_matrix(G, attribute):
    # Get all unique values of the attribute
    attribute_values = set(nx.get_node_attributes(G, attribute).values())
    
    # Initialize the mixing matrix
    num_values = len(attribute_values)
    mixing_matrix = np.zeros((num_values, num_values), dtype=int)
    
    # Create a dictionary to map attribute values to matrix indices
    value_to_index = {value: i for i, value in enumerate(attribute_values)}
    
    # Iterate over all edges in the graph
    for u, v in G.edges():
        attr_u = G.nodes[u][attribute]
        attr_v = G.nodes[v][attribute]
        i = value_to_index[attr_u]
        j = value_to_index[attr_v]
        mixing_matrix[i][j] += 1
        if i != j:
            mixing_matrix[j][i] += 1
    
    return mixing_matrix

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
# nx.set_node_attributes(G, {1: 'A', 2: 'A', 3: 'B', 4: 'B'}, 'group')
# print(mixing_matrix(G, 'group'))
