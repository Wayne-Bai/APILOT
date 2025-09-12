import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
for i in range(5):
    G.add_node(str(i))

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
G.add_edges_from(edges)

# Get nodes in order of addition
print("Nodes in order of addition:")
print(G.nodes)

# Get edges in order of addition
print("\nEdges in order of addition:")
print(G.edges)

# Get nodes in sorted order
print("\nNodes in sorted order:")
sorted_nodes = sorted(G.nodes)
print(sorted_nodes)

# Get edges in sorted order
print("\nEdges in sorted order:")
sorted_edges = sorted(G.edges)
print(sorted_edges)
