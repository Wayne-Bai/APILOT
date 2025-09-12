import networkx as nx

# Create an empty directed graph
G = nx.DiGraph()

# Define the graph description
# Nodes: (A, B, C, D)
# Edges: (A->B, B->C, C->B, A->D, B->A, C->D)

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Add edges
edges = [('A', 'B'), ('B', 'C'), ('C', 'B'), ('A', 'D'), ('B', 'A'), ('C', 'D')]
G.add_edges_from(edges)

# Display the graph
print("Graph description:")
for node in G.nodes:
    print(f"Node: {node}")
for edge in G.edges:
    print(f"Edge: {edge[0]} -> {edge[1]}")
