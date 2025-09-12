
import networkx as nx

# Define the graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Compute the Google matrix
google_matrix = nx.google_matrix(G)

# Print the Google matrix
print(google_matrix.todense())
