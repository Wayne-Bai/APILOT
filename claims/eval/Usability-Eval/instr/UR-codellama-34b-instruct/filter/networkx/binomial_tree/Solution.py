
import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    for i in range(1, n+1):
        G.add_node(i)
        for j in range(1, i):
            if j < i-j:
                G.add_edge(i, j)
                G.add_edge(j, i)
    return G
