import networkx as nx
import osmnx as ox
# Load the graph from OpenStreetMap
G = ox.graph_from_place('Pittsburgh, PA', network_type='drive')
# Remove all nodes and edges that do not have a geometry (i.e., no Wkb or Wkt key)
G.remove_nodes_from([n for n in G.nodes() if not G.nodes[n].get('geometry')])
G.remove_edges_from([e for e in G.edges() if not G.edges[e].get('geometry')])
# Save the nodes and edges as shapefiles
ox.save_graph_shapefile(G, filename='pittsburgh')
