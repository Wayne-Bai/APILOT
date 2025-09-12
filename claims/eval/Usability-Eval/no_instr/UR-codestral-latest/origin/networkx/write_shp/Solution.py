import networkx as nx
import shapefile
from shapely.wkt import loads

# Assuming G is your DiGraph
G = nx.DiGraph()

# Writing nodes to a shapefile
w = shapefile.Writer('nodes')
w.field('node_id', 'N')
for node, data in G.nodes(data=True):
    w.point(*loads(data['Wkt']).coords[0])
    w.record(node_id=node)
w.close()

# Writing edges to a shapefile
w = shapefile.Writer('edges')
w.field('start_node', 'N')
w.field('end_node', 'N')
for u, v, data in G.edges(data=True):
    w.line([*loads(data['Wkt']).coords])
    w.record(start_node=u, end_node=v)
w.close()
