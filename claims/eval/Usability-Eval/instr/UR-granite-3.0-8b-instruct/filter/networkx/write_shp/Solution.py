import networkx as nx
from networkx.readwrite import json_graph
import geopandas as gpd
from shapely.geometry import Point

# Assuming G is your networkx.DiGraph
nodes = G.nodes(data=True)
edges = G.edges(data=True)

# Create a GeoDataFrame for nodes
node_geometry = [Point(node_data['wkb'][:]) if 'wkb' in node_data else Point(node_data['x'], node_data['y']) for node, node_data in nodes.items()]
node_df = gpd.GeoDataFrame({'node_id': list(nodes.keys())}, geometry=node_geometry)

# Create a GeoDataFrame for edges
edge_geometry = [LineString(edge_data['wkb'][:]) if 'wkb' in edge_data else LineString([G.nodes[u]['x'], G.nodes[v]['x']]) for u, v, edge_data in edges.items()]
edge_df = gpd.GeoDataFrame({'edge_id': list(edges.keys())}, geometry=edge_geometry)

# Save to shapefiles
node_df.to_file("nodes.shp")
edge_df.to_file("edges.shp")
