import networkx as nx

def binomial_tree(n):
    """Returns the Binomial Tree of order n."""
    G = nx.Graph()
    G.add_node(0)
    for i in range(1, n+1):
        for j in range(i):
            G.add_node(i*10+j)
            G.add_edge(i*10+j, i*10+j-1)
            G.add_edge(i*10+j, i*10+j+1)
    return G
