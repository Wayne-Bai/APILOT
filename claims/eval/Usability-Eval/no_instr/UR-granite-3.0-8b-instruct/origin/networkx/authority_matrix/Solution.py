import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('node1', 'node2')
G.add_edge('node2', 'node3')

# Calculate HITS authority matrix
authority_matrix = nx.hits(G)

print(authority_matrix)
