import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Iterate over the edges in the graph
for u, v in G.edges():
    print(f"({u}, {v})")
