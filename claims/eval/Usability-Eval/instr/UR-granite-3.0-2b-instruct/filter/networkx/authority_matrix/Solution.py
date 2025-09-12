import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('A', 'B', weight=0.5)
G.add_edge('A', 'C', weight=0.2)
G.add_edge('B', 'C', weight=0.8)
G.add_edge('B', 'D', weight=0.3)
G.add_edge('C', 'D', weight=0.7)

# Calculate HITS matrix
hits_authority = nx.hits(G, alpha=0.5)

# Print the HITS authority matrix
print(hits_authority)
