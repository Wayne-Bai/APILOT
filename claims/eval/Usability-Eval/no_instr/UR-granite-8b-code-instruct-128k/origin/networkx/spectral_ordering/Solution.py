import networkx as nx
def spectral_ordering(graph):
    fiedler_vector = nx.fiedler_vector(graph)
    sorted_nodes = sorted(graph.nodes(), key=lambda node: fiedler_vector[node])
    return sorted_nodes
