
import networkx as nx
from shapely.geometry import LineString, Point
import geopandas as gpd

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([(1, {'name': 'A'}), (2, {'name': 'B'}), (3, {'name': 'C'})])
G.add_edges_from([(1, 2), (2, 3)])

# Create a GeoDataFrame for the edges
edge_gdf = gpd.GeoDataFrame(geometry=[LineString(G.edges[e]['geometry']) for e in G.edges()], crs=G.graph['crs'])

# Create a GeoDataFrame for the nodes
node_gdf = gpd.GeoDataFrame(geometry=[Point(G.nodes[n]['x'], G.nodes[n]['y']) for n in G.nodes()], crs=G.graph['crs'])

# Write the edge GeoDataFrame to a shapefile
edge_gdf.to_file('edges.shp')

# Write the node GeoDataFrame to a shapefile
node_gdf.to_file('nodes.shp')
