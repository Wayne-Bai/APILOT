import networkx as nx

# Assume you have a graph G defined here
# G = nx.Graph()
# ... add nodes and edges to the graph ...

# Calculating the average degree connectivity using NetworkX
degrees = [val for (node, val) in G.degree()]
num_nodes = G.number_of_nodes()
avg_degree_connectivity = sum(degrees) / num_nodes

print("Average degree connectivity of the graph: ", avg_degree_connectivity)
