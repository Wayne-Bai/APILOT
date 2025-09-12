import networkx as nx

def generate_random_graph_barabasi_albert(n, m):
    G = nx.barabasi_albert_graph(n, m)
    return G
