
import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Convert the graph to a matrix
A = nx.to_numpy_matrix(G)

print(A)
