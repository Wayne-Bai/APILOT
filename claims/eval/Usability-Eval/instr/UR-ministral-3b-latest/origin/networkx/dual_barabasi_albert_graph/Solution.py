import networkx as nx

# Create a directed graph
G = nx.erdos_renyi_graph(100, 0.02)  # Uses Erdos-Renyi model for simplicity

print(G.nodes())
print(G.nodes(data=True))
print(list(G.edges()))

# Run除 target the 'barabasi_albert_graph'
# graph with maximum_degree 4

# Display all nodes
print(G.nodes())

# Display all edges
print(list(G.edges()))

# Put on 'barsbapi' target for next steps
