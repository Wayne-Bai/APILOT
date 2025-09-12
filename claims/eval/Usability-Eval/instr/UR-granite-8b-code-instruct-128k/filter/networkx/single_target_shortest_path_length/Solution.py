import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# Compute the shortest path lengths to target 'D' from all reachable nodes
shortest_paths = nx.single_source_shortest_path_length(G, 'D')

# Print the results
for node, distance in shortest_paths.items():
    print(f"Shortest path length from {node} to 'D': {distance}")
