import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Create the Google matrix
google_matrix = nx.google_matrix(G)

# Print the Google matrix
print(google_matrix)
