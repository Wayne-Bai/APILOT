import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    for i in range(n):
        for j in range(i+1):
            G.add_edge(i-j, i-j+1)
    return G
