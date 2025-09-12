
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph

# Compute the shortest path lengths to target from all reachable nodes
shortest_paths = nx.shortest_path_length(G, target=3)

print(shortest_paths)
