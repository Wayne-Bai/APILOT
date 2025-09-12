import networkx as nx

graph_description = {'A': ['B', 'C'],
                     'B': ['A', 'D', 'E'],
                     'C': ['A', 'F'],
                     'D': ['B'],
                     'E': ['B', 'F'],
                     'F': ['C', 'E']}

# Create a graph
G = nx.Graph()

# Add nodes and edges to graph
for node, neighbors in graph_description.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

G
