import networkx as nx
def dual_barabasi_albert_graph(n, m1, m2, p):
    G = nx.dual_barabasi_albert_graph(n, m1, m2, p)
    return G