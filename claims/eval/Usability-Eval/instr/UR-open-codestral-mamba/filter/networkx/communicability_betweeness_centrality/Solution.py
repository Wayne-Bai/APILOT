import networkx as nx

# Create a sample graph for demonstration
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)

# Calculate communicability between all pairs of nodes
communicability = nx.communicability(G)

# Print the communicability scores
for i in communicability:
    for j in communicability:
        print(f"Communicability between node {i} and node {j}: {communicability[i][j]}")
