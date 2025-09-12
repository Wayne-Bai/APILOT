import networkx as nx
# Create a graph
G = nx.Graph()
# Add nodes and edges
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')])
# Compute shortest paths from node A to all other nodes
shortest_paths = nx.shortest_path(G, source='A')
print(shortest_paths)
