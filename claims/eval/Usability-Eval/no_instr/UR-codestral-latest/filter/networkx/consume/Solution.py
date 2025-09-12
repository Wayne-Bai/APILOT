import networkx as nx

# Create a graph
G = nx.Graph()

# Add some nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add some edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Get an iterator of the nodes in the graph
node_iterator = iter(G.nodes())

# Consume the iterator entirely
try:
    while True:
        print(next(node_iterator))
except StopIteration:
    print("Iterator is consumed.")
