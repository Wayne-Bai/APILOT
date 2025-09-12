import networkx as nx
import numpy as np

def numeric_mixing_matrix(G, attribute):
    # Get all unique values of the attribute
    attribute_values = set(nx.get_node_attributes(G, attribute).values())
    
    # Initialize the mixing matrix
    mixing_matrix = np.zeros((len(attribute_values), len(attribute_values)), dtype=int)
    
    # Create a dictionary to map attribute values to matrix indices
    attribute_to_index = {value: i for i, value in enumerate(attribute_values)}
    
    # Iterate over all edges in the graph
    for u, v in G.edges():
        attr_u = G.nodes[u][attribute]
        attr_v = G.nodes[v][attribute]
        i = attribute_to_index[attr_u]
        j = attribute_to_index[attr_v]
        mixing_matrix[i][j] += 1
        if i != j:
            mixing_matrix[j][i] += 1
    
    return mixing_matrix
