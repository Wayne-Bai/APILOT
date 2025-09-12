import networkx as nx

# Assuming G is your graph and 'target' is the target node
G = nx.Graph()  # replace with your graph
target = 'target_node'  # replace with your target node

# Compute shortest path lengths to target from all reachable nodes
shortest_paths = nx.dijkstra_path_length(G, target)

# Print the results
for node in G.nodes():
    if node != target:
        print(f"The shortest path length from {node} to {target} is {shortest_paths[node]}")
