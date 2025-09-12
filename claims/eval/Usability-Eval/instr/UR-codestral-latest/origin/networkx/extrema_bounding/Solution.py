import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph. For example:
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'D', weight=3)
G.add_edge('D', 'A', weight=4)

# Calculate diameter
diameter = nx.diameter(G)

# Calculate radius
radius = nx.radius(G)

# Calculate eccentricity
eccentricity = nx.eccentricity(G)

# Calculate periphery
periphery = nx.periphery(G)

# Calculate center
center = nx.center(G)
