import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['Node1', 'Node2', 'Node3'])

# Draw the graph
nx.draw(G, with_labels=True)
