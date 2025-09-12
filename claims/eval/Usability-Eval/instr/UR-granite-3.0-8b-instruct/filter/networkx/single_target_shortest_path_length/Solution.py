import networkx as nx

# Assuming G is your graph
shortest_paths = nx.single_source_shortest_path_length(G, target_node)

for node, length in shortest_paths.items():
    print(f"The shortest path from {node} to the target node is {length} steps.")
