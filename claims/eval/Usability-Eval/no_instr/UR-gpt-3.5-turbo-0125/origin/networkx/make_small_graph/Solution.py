
import networkx as nx

# Graph description: Create a small graph with 4 nodes and 4 edges
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

print("Nodes of the graph:", G.nodes())
print("Edges of the graph:", G.edges())
