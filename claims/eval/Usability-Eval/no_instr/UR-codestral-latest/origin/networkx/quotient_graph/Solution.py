import networkx as nx
from networkx.algorithms.equivalence import quotient_graph

# Create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Define the equivalence relation
partitions = [{1, 2}, {3, 4, 5}]

# Get the quotient graph
Q = quotient_graph(G, partitions)
