
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Consume the iterator entirely
for _ in nx.generate_adjlist(G):
    pass
