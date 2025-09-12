
import networkx as nx

# Create an undirected graph G
G = nx.Graph()

# Adding nodes to the graph
G.add_nodes_from([1, 2, 3, 4])

# Adding edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Computing the requested extreme distance metric of the graph G
eccentricity_dict = nx.eccentricity(G)
print("Eccentricity of nodes in G:", eccentricity_dict)
