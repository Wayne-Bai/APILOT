import networkx as nx

def binomial_tree(n):
    B = nx.Graph()
    for i in range(n):
        for j in range(2 ** i):
            B.add_edge(j, j + 2 ** i)
    return B

# Example: Create a Binomial Tree of order 4
B_tree = binomial_tree(4)
print("Nodes:", B_tree.nodes())
print("Edges:", B_tree.edges())
