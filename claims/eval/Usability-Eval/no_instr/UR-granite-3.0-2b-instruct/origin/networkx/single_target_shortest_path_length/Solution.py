import networkx as nx

# Assuming G is your graph and 'target' is the node you want to find the shortest path to
G = nx.Graph()  # replace with your graph
target = 'target_node'  # replace with the target node

# Compute shortest path lengths to target from all reachable nodes
shortest_path_lengths = nx.single_source_shortest_path_length(G, target)

print(shortest_path_lengths)
