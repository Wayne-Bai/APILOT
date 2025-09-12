
import networkx as nx

def generate_binomial_tree(n):
    G = nx.Graph()
    G.add_node(0)
    if n > 0:
        G.add_node(1)
        G.add_edge(0, 1)
    if n > 1:
        G.add_node(2)
        G.add_edge(1, 2)
        for i in range(2, n+1):
            G.add_node(i)
            G.add_edge(0, i)
            for j in range(1, i):
                G.add_edge(j, i)
    return G
