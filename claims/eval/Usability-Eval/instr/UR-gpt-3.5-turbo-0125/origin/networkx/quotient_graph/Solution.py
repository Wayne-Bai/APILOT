
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (4, 5)])

# Define an equivalence relation on nodes
equivalence = {1: [1, 2, 3], 4: [4, 5]}

# Create the quotient graph
quotient = nx.quotient_graph(G, equivalence)

print(quotient.nodes())
