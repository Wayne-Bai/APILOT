import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('A', 'B', weight=2)
G.add_edge('B', 'C', weight=3)
G.add_edge('A', 'C', weight=1)

# Compute the Google matrix of the graph
google_matrix = nx.google_matrix(G)

print(google_matrix.todense())
