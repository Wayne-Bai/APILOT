import networkx as nx

# Assuming G is your undirected graph
G = nx.Graph()

# Add nodes and edges to your graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("A", "C")

# Compute the shortest path between all pairs of nodes
shortest_paths = nx.all_pairs_shortest_path(G)

# Compute the maximum distance between any two nodes
max_distance = max(shortest_paths)

print("The maximum distance in the graph is:", max_distance)
