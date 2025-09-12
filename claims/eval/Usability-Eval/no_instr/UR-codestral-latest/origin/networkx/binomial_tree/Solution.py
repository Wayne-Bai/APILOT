import networkx as nx

def generate_binomial_tree(n):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges
    for i in range(n):
        for j in range(i+1, n+1):
            G.add_edge(j, i)

    return G

n = 5  # order of the Binomial Tree
G = generate_binomial_tree(n)
