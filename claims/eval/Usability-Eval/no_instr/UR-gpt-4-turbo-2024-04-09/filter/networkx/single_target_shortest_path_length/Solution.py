import networkx as nx

# Create a graph
G = nx.Graph()
# Add some edges to the graph
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('A', 'D', weight=4)

# Define the target node
target_node = 'D'

# Compute the shortest path lengths from all nodes to the target node
path_lengths = {node: nx.shortest_path_length(G, source=node, target=target_node, weight='weight') for node in G.nodes}

print(path_lengths)
