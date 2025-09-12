import networkx as nx

# Generate a Barabási–Albert random graph
n = 10  # Number of nodes
m = 2   # Number of edges to attach from a new node to existing nodes
G = nx.barabasi_albert_graph(n, m)

# Print the graph
print(G.edges())
