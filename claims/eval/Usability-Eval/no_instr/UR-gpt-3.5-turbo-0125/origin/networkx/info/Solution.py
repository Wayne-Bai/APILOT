
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Print short summary of the graph
print(nx.info(G))
