import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Get an iterator for the nodes in the graph
node_iterator = iter(G.nodes)

# Consume the iterator entirely
for node in node_iterator:
    print(node)
