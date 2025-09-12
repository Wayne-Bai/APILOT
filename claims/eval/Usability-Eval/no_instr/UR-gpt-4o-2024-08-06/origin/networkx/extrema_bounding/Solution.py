import networkx as nx

# Create an example undirected graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# Compute the extreme distance metric (diameter of the graph)
# The diameter is the longest shortest path between any two nodes in the graph.
diameter = nx.diameter(G)

# Compute the eccentricity of all nodes
eccentricity = nx.eccentricity(G)

# Output the extreme distance metric details
print(f"Diameter of the graph: {diameter}")
print(f"Eccentricity of all nodes: {eccentricity}")
