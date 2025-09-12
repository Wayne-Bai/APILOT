import networkx as nx
import matplotlib.pyplot as plt

def dual_barabasi_albert_graph(n, m1, m2, seed=None):
    # Creating two Barabási–Albert graphs
    G1 = nx.barabasi_albert_graph(n, m1, seed=seed)
    G2 = nx.barabasi_albert_graph(n, m2, seed=seed)

    # Combining the two graphs
    G = nx.union(G1, G2, rename=('G1-', 'G2-'))

    # Optional: Connecting corresponding nodes from G1 and G2
    for i in range(n):
        G.add_edge(f'G1-{i}', f'G2-{i}')

    return G

# Example usage:
n = 100  # Number of nodes
m1 = 2   # Number of edges to attach from a new node to existing nodes in G1
m2 = 3   # Number of edges to attach from a new node to existing nodes in G2

# Create the graph
G = dual_barabasi_albert_graph(n, m1, m2)

# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(G, node_size=20, with_labels=False)
plt.show()
