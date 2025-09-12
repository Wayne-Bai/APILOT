import networkx as nx

# Create a simple graph with four nodes and three edges
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D')])

# Compute shortest paths from node 'A' to all other nodes in the graph
shortest_paths = nx.shortest_path(G, source='A')

# Print the shortest path from 'A' to each other node in the graph
for node in G.nodes:
    if node != 'A':
        print(f"Shortest path from A to {node}: {shortest_paths[node]}")
