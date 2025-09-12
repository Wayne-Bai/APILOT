
import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    for i in range(n + 1):
        for j in range(i):
            G.add_edge((i, j), (i - 1, j))
            G.add_edge((i, j), (i - 1, j + 1))
    return G

# Example usage
n = 3
T = binomial_tree(n)
nx.draw(T, with_labels=True)
