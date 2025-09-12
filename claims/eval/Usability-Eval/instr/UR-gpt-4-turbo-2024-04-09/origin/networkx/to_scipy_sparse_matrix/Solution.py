import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)

# Get the adjacency matrix as a SciPy sparse matrix
adjacency_matrix = nx.adjacency_matrix(G)

print(adjacency_matrix)
