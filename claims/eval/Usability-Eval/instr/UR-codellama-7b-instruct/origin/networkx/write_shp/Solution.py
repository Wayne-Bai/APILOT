
import networkx as nx

# create a sample graph
G = nx.DiGraph()
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_node(3)
G.nodes[3]['x'] = 4
G.nodes[3]['y'] = 5

# write the graph to two shapefiles
nx.write_shp(G, 'edges', edge_key='geometry')
nx.write_shp(G, 'nodes', node_key='geometry')
