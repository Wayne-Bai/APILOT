
import networkx as nx

def binomial_tree(n):
    g = nx.Graph()
    for i in range(1, n+1):
        g.add_node(i)
        if i > 1:
            g.add_edge(i, i-1)
        if i < n:
            g.add_edge(i, i+1)
    return g
