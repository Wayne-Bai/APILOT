import networkx as nx

def generate_binomial_tree(n):
    G = nx.DiGraph()
    G.add_node(0)
    for i in range(1, n+1):
        G.add_node(i)
        G.add_edge(i//2, i)
    return G
