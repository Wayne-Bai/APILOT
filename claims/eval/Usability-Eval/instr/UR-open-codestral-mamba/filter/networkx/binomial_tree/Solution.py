import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    nodes = [(i, {}) for i in range(2**n)]
    G.add_nodes_from(nodes)
    for i in range(n):
        for j in range(2**i):
            G.add_edge((j, i), (2*j, i+1))
            G.add_edge((j, i), (2*j+1, i+1))
    return G

print(binomial_tree(3))
