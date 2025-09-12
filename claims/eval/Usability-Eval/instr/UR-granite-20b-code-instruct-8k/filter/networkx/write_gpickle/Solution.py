import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 3)])

# Write the graph in Python pickle format
nx.write_gpickle(G, 'graph.pickle')
