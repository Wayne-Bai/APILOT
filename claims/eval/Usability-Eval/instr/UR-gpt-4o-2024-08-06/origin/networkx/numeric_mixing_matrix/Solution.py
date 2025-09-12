import networkx as nx
import numpy as np

def numeric_mixing_matrix(G, attribute):
    attribute_values = [data.get(attribute) for _, data in G.nodes(data=True)]
    unique_values = list(set(attribute_values))
    value_to_index = {value: idx for idx, value in enumerate(unique_values)}
    matrix_size = len(unique_values)
    
    mixing_matrix = np.zeros((matrix_size, matrix_size))

    for u, v in G.edges():
        u_attr = G.nodes[u].get(attribute)
        v_attr = G.nodes[v].get(attribute)
        if u_attr is not None and v_attr is not None:
            u_idx = value_to_index[u_attr]
            v_idx = value_to_index[v_attr]
            mixing_matrix[u_idx, v_idx] += 1

    return mixing_matrix

# Example usage:
# G = nx.Graph()
# G.add_node(1, type='A')
# G.add_node(2, type='B')
# G.add_node(3, type='A')
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(2, 3)
# print(numeric_mixing_matrix(G, 'type'))
