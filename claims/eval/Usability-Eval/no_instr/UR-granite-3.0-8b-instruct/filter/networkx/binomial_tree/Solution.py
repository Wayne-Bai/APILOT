import networkx as nx

def binomial_tree(n):
    if n <= 0:
        return nx.Graph()
    else:
        # Create the root node
        G = nx.Graph()
        G.add_node(0)

        # Recursively add child nodes
        for i in range(1, n+1):
            G.add_node(i)
            G.add_edge(i-1, i)

        return G
