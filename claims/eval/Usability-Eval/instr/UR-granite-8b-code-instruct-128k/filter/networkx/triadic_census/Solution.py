import networkx as nx

def triadic_census(G, nodes=None):
    if nodes is None:
        nodes = G.nodes()

    census = nx.utils.triads.triadic_census(G, nodes)
    return census
