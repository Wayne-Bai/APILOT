import networkx as nx

# Creating a directed graph
G = nx.DiGraph()

# Adding edges to the graph
G.add_edge('A', 'B', weight=5)
G.add_edge('B', 'C', weight=3)
G.add_edge('B', 'D', weight=8)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=1)

# Calculating shortest path lengths
shortest_path_lengths = nx.single_source_shortest_path_length(G, 'A')

print(shortest_path_lengths)
