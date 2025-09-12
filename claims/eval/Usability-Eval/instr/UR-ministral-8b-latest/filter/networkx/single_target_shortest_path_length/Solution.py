import networkx as nx

def compute_shortest_path_lengths(G, source):
    # Compute shortest path lengths from the source node to all reachable nodes
    shortest_paths = nx.single_source_dijkstra_path_length(G, source)
    return shortest_paths

# Example: Define a graph
G = nx.Graph()
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=5)
G.add_edge(3, 4, weight=1)

# Define the source node
source_node = 1

# Compute shortest path lengths from source_node
shortest_paths_lengths = compute_shortest_path_lengths(G, source_node)

# Print the shortest path lengths
for node in shortest_paths_lengths:
    print(f"Shortest path length from {source_node} to {node}: {shortest_paths_lengths[node]}")
