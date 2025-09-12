import networkx as nx
import matplotlib.pyplot as plt

# Function to create Binomial Tree of order n
def binomial_tree(n):
    G = nx.Graph()
    nodes = [(i, j) for i in range(n+1) for j in range(i+1)]
    G.add_nodes_from(nodes)
    for i in range(n):
        for j in range(i+1):
            G.add_edge((i,j), (i+1, j))
            G.add_edge((i,j), (i+1, j+1))
    return G

# Test the function with order 3
G = binomial_tree(3)

# Draw and show the binomial tree
nx.draw(G, with_labels=True)
plt.show()
