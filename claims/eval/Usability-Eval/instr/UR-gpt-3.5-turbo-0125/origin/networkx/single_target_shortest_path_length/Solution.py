
import networkx as nx

# create a graph
G = nx.Graph()

# add nodes
G.add_nodes_from([1, 2, 3, 4])

# add edges
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

# Compute the shortest path lengths to a target node from all reachable nodes
target_node = 4
shortest_path_lengths = dict(nx.shortest_path_length(G, target_node=target_node))

print(shortest_path_lengths)
