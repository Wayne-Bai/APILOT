
import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    for i in range(n-1):
        G.add_edge((i, i+1))
    for j in range(n-2):
        G.add_edge((j+1, j))
    return G
