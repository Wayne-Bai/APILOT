import networkx as nx

# Create an ordered directed graph
G = nx.DiGraph()

# Add nodes and edges in a specific order
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Print the nodes and edges in the order they were added
for node in G.nodes():
    print(node)

for edge in G.edges():
    print(edge)
