
import networkx as nx

# Define the graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2, weight=0.5)
G.add_edge(2, 3, weight=0.8)
G.add_edge(3, 4, weight=1.2)
G.add_edge(4, 5, weight=1.5)
G.add_edge(5, 1, weight=2.0)

# Compute the shortest path lengths to target from all reachable nodes
shortest_path_lengths = nx.single_source_shortest_path_length(G, source=1, target=5)

# Print the shortest path lengths
for node, length in shortest_path_lengths.items():
    print(f"Shortest path length from node 1 to node {node}: {length}")
