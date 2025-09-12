
import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Compute the diameter of the graph
eccentricities = nx.eccentricity(G)
diameter = max(eccentricities.values())

print("The diameter of the graph is:", diameter)
