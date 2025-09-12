import networkx as nx
import matplotlib.pyplot as plt

def create_binomial_tree(n):
    """
    Creates a binomial tree of order n.
    
    Parameters:
    n (int): Order of the binomial tree.
    
    Returns:
    nx.DiGraph: A directed graph representing the binomial tree.
    """
    G = nx.DiGraph()
    for i in range(n+1):
        for j in range(2**i):
            if i > 0:
                G.add_edge((i-1, j//2), (i, j))
            G.add_node((i, j))
    return G

# Example usage
n = 3
G = create_binomial_tree(n)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
plt.show()
