
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph with weights
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 4, weight=1)
G.add_edge(3, 5, weight=2)
G.add_edge(4, 5, weight=3)

# Compute shortest paths in the graph
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
print(shortest_paths)
