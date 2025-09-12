import networkx as nx
import numpy as np

def get_attribute_matrix(G):
    if 'attribute' in dir(G):
        attributes = G.attribute
        num_nodes = len(attributes)
        attribute_matrix = np.zeros((num_nodes, num_nodes))

        for i in range(num_nodes):
            for j in range(num_nodes):
                attribute_matrix[i, j] = attributes[G.edges[i, j]['attribute']]

        return attribute_matrix
    else:
        raise ValueError("Graph G does not have an 'attribute' attribute")
