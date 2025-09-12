import networkx as nx

def attribute_mixing_matrix(G):
    nodes = G.nodes()
    attributes = {n: attr for n, attr in G.nodes(data=True)}

    unique_attributes = set([attr for attr_dict in attributes.values() for attr in attr_dict.values()])

    mixing_matrix = {}

    for attr in unique_attributes:
        mixing_matrix[attr] = {}
        for attr2 in unique_attributes:
            mixing_matrix[attr][attr2] = 0

    for node, attr_dict in attributes.items():
        for attr in attr_dict.values():
            for neighbor in G.neighbors(node):
                for neighbor_attr in attributes[neighbor].values():
                    mixing_matrix[attr][neighbor_attr] += 1

    for attr in unique_attributes:
        total = sum(mixing_matrix[attr].values())
        for attr2 in unique_attributes:
            mixing_matrix[attr][attr2] /= total

    return mixing_matrix
