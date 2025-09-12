
import networkx as nx

# Create a DiGraph object
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Compute the shortest path lengths from node 1 to all other nodes in the graph
shortest_path_lengths = nx.shortest_path_length(G, source=1)

# Print the shortest path lengths
for i in range(len(shortest_path_lengths)):
    print("Shortest path length from node 1 to node", i+1, ":", shortest_path_lengths[i])
