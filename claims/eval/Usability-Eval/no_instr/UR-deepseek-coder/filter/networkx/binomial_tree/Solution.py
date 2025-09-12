import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    G.add_node(0)
    
    for i in range(n):
        for j in range(2**i):
            G.add_edge(j, 2**i + j)
            G.add_edge(j, 2**i + j + 1)
    
    return G

# Example usage:
# n = 3
# tree = binomial_tree(n)
# print(tree.edges())
