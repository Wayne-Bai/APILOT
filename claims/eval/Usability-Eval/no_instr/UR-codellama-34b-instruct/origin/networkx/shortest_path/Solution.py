
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])

# Compute shortest paths from node A to all other nodes
shortest_paths = nx.dijkstra_path(G, 'A')

# Print the shortest path from A to each other node
for i in range(len(G)):
    print(f'Shortest path from A to {G[i]} is: {shortest_paths[i][0]}')
