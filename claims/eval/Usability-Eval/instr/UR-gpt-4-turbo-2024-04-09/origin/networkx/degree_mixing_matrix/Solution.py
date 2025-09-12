import networkx as nx

def attribute_mixing_matrix(G, attribute):
    # This function returns a mixing matrix for the node attribute.
    # G: Graph
    # attribute: Node attribute (for example "gender", "age" etc.)
    return nx.attribute_mixing_matrix(G, attribute)
