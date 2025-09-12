import networkx as nx

# Generate a random graph using dual Barabasi-Albert preferential attachment
def generate_random_graph(n, m1, m2):
    G = nx.dual_barabasi_albert_graph(n, m1, m2)
    return G

# Example usage
n = 10  # Number of nodes
m1 = 2  # Number of edges to attach from a new node to existing nodes
m2 = 1  # Number of edges to attach from a new node to existing nodes for the second attachment
G = generate_random_graph(n, m1, m2)

# Plot the graph using NetworkX's built-in function
nx.draw(G, with_labels=True)
