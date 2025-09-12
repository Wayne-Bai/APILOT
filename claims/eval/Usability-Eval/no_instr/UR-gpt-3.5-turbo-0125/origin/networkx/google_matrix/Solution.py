
import networkx as nx

# Create a graph
G = nx.DiGraph()
edges = [(1, 2), (2, 3), (3, 1)]
G.add_edges_from(edges)

# Returns the Google matrix of the graph
n = len(G)
d = 0.85  # Damping factor
alpha = 1 / n
matrix = alpha * nx.to_numpy_matrix(G).T + (1-alpha) / n

print(matrix)
