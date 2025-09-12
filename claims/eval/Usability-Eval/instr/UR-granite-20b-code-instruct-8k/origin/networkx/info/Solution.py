import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# Print a summary of the graph
print(nx.info(G))

# Find the shortest path from node 1 to node 4
path = nx.shortest_path(G, 1, 4)
print("Shortest path from node 1 to node 4:", path)
