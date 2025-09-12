import networkx as nx

# Create an empty directed graph
G = nx.DiGraph()

# Add 5 nodes (0 to 4) to the graph
for i in range(5):
    G.add_node(i)

# Connect nodes from 0 to 4 in a cycle
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])

# Create an iterator over the nodes and edges in the graph
node_iter = nx.nodes(G)
edge_iter = nx.edges(G)

# Consume the iterator entirely
for node in node_iter:
    print(node)  # Print each node

for edge in edge_iter:
    print(edge)  # Print each edge
