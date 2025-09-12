import networkx as nx

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=3)

# Get the adjacency matrix
adj_matrix = nx.adj_matrix(G)
print(adj_matrix)
