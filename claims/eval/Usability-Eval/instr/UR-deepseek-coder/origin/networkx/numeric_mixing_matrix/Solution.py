import networkx as nx
import numpy as np

def numeric_mixing_matrix(G, attribute):
    # Get all unique attribute values
    attribute_values = set(nx.get_node_attributes(G, attribute).values())
    
    # Initialize the mixing matrix
    mixing_matrix = np.zeros((len(attribute_values), len(attribute_values)), dtype=int)
    
    # Create a mapping from attribute value to matrix index
    value_to_index = {value: idx for idx, value in enumerate(attribute_values)}
    
    # Iterate over all edges in the graph
    for u, v in G.edges():
        attr_u = G.nodes[u][attribute]
        attr_v = G.nodes[v][attribute]
        mixing_matrix[value_to_index[attr_u], value_to_index[attr_v]] += 1
        if u != v:  # Ensure we don't double-count self-loops
            mixing_matrix[value_to_index[attr_v], value_to_index[attr_u]] += 1
    
    return mixing_matrix

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
# nx.set_node_attributes(G, {1: {'color': 'red'}, 2: {'color': 'blue'}, 3: {'color': 'red'}, 4: {'color': 'blue'}})
# print(numeric_mixing_matrix(G, 'color'))
