import networkx as nx
import numpy as np

def get_mixing_matrix(graph, attribute):
    # Fetch the attribute values from the graph
    attribute_values = nx.get_node_attributes(graph, attribute)

    # Create a dictionary to store the indices of each unique attribute value
    indices = {}
    for i, value in enumerate(attribute_values.values()):
        if value not in indices:
            indices[value] = []
        indices[value].append(i)

    # Initialize the mixing matrix with zeros
    mixing_matrix = np.zeros((len(attribute_values), len(attribute_values)))

    # Iterate over each node in the graph and update the mixing matrix
    for node in graph.nodes():
        value = attribute_values[node]
        for index in indices[value]:
            mixing_matrix[index, node] = 1

    # Normalize the mixing matrix by the number of nodes with each attribute value
    row_sums = mixing_matrix.sum(axis=1)
    mixing_matrix = mixing_matrix / row_sums[:, np.newaxis]

    return mixing_matrix
