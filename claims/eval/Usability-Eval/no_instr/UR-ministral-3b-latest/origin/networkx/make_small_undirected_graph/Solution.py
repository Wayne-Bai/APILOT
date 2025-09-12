import networkx as nx

# Create a new graph
G = nx.Graph()

# Add edges to the graph described in graph_description
graph_description = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'A'),
    ('D', 'E')
]

for edge in graph_description:
    G.add_edge(edge[0], edge[1])

# Output the graph
print("Graph Edge List:", list(G.edges))
print("Graph Node List:", G.nodes)
