
import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    
    if n == 0:
        return G
    
    G.add_node((0, 0))
    
    for i in range(1, n+1):
        for j in range(0, i+1):
            G.add_node((i, j))
            if j > 0:
                G.add_edge((i, j), (i-1, j-1))
            if j < i:
                G.add_edge((i, j), (i-1, j))
    
    return G

n = 4
binomial_tree_graph = binomial_tree(n)
print("Nodes:", binomial_tree_graph.nodes())
print("Edges:", binomial_tree_graph.edges())
