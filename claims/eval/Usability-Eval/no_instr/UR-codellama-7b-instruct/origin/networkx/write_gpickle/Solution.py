import networkx as nx
G = nx.Graph()
# add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('A', 'C')])
# save the graph to a pickle file
nx.write_gpickle(G, 'graph.pkl')
