import networkx as nx

# Create a graph
G = nx.Graph()

# Add some edges
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')]
G.add_edges_from(edges)

# Define the source node
source = 'A'

# Compute the shortest path lengths to the source node
shortest_paths = nx.single_source_shortest_path_length(G, source)

# Print the result
for node, length in shortest_paths.items():
    print(f'The shortest path length to {node} is {length}')
