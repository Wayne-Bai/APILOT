import networkx as nx
import numpy as np

def adjacency_matrix_with_attributes(G):
    if not G.is_directed():
        dir_g = G.to_directed()
        adj_mat = nx.attr_matrix(dir_g, node_attr='attribute_name', normalized=False, dtype=None).astype(np.int) # replace 'attribute_name' with the actual attribute name
    else:
        adj_mat = nx.attr_matrix(G, node_attr='attribute_name', normalized=False, dtype=None).astype(np.int) # replace 'attribute_name' with the actual attribute name
    return adj_mat
