import networkx as nx
G = nx.Graph()
# Add nodes to the graph G
# Node names should be provided in a list
node_list = ['Node1', 'Node2', 'Node3']
G.add_nodes_from(node_list)
# Draw the graph
nx.draw(G, with_labels=True)
