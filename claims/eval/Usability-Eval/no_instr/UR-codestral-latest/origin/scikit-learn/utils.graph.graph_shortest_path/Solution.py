import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
# Example: Adding edges (1, 2), (1, 3), (2, 4), (3, 4)
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
G.add_edges_from(edges)

# Perform shortest-path graph search
# Example: Shortest path between node 1 and node 4
shortest_path = nx.shortest_path(G, source=1, target=4)
print(f'Shortest path: {shortest_path}')
