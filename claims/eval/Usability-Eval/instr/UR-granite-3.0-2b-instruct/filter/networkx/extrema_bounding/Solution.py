import networkx as nx

# Assuming G is an undirected graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("A", "C")

# Compute the shortest path between all pairs of nodes
shortest_paths = nx.all_pairs_shortest_path(G)

# Compute the maximum distance between any two nodes
max_distance = max(max(d[i] for i in G.nodes) for d in shortest_paths)

print("Maximum distance in the graph:", max_distance)
