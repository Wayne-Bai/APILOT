import networkx as nx

# create a graph
G = nx.Graph()

# Add edges to the graph with their respective weights
edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3), ("C", "D", 4)]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# find the shortest path from node 'A' to node 'D'
shortest_path = nx.shortest_path(G, source="A", target="D", weight="weight")
print(f"The shortest path is: {shortest_path}")
