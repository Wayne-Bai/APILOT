import networkx as nx

def create_small_graph(graph_description):
    G = nx.Graph()
    G.add_edges_from(graph_description)
    return G
