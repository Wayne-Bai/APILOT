import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('A', 'B', weight=0.1)
G.add_edge('A', 'C', weight=0.2)
G.add_edge('B', 'C', weight=0.3)
G.add_edge('B', 'D', weight=0.4)
G.add_edge('C', 'D', weight=0.5)

# Calculate HITS matrix
hits = nx.hits(G, beta=0.85)

# Print the HITS authority matrix
print(hits.authority())
