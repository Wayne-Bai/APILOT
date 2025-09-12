import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)

# Calculate HITS matrix
hubs, authorities = nx.hits(G)

# Print the HITS matrix
print("Hubs:")
print(hubs)
print("\nAuthorities:")
print(authorities)
