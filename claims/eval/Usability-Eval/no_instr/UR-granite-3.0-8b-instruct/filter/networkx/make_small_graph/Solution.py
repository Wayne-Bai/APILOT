import networkx as nx

# Define the graph description
graph_description = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for node, neighbors in graph_description.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Return the small graph
return G
