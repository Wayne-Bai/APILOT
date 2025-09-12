
import networkx as nx
import random

def generate_dual_BA_graph(n, m):
    G = nx.empty_graph(n)
    for i in range(m):
        while True:
            a = random.randint(0, n-1)
            b = random.randint(0, n-1)
            if not G.has_edge(a, b):
                break
        G.add_edge(a, b)
    return G
