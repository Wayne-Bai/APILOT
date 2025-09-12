import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    G.add_node(1)
    for i in range(2, n+1):
        G.add_node(i)
        for j in range(1, i):
            G.add_edge(j, i)
    return G
