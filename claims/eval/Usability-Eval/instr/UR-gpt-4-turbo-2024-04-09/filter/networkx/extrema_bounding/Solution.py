import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Add some edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('E', 'A')

# Function to compute the diameter of the graph
def compute_diameter(graph):
    # Generate all pairs shortest path lengths
    all_pair_shortest_path_length = dict(nx.all_pairs_shortest_path_length(graph))
    
    # Find the maximum distance in the shortest path length dictionary
    diameter = max(max(lengths.values()) for lengths in all_pair_shortest_path_length.values())
    return diameter

# Compute the diameter of the graph
diameter = compute_diameter(G)

print("Diameter of the graph:", diameter)
