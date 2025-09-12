import networkx as nx
from shapely.geometry import Point, LineString
import geopandas as gpd
from pyproj import CRS

def write_to_shapefiles(G, nodes_file, edges_file):
    # Nodes
    node_geom = [Point(data['x'], data['y']) for node, data in G.nodes(data=True)]
    nodes_gdf = gpd.GeoDataFrame({'id': list(G.nodes)}, geometry=node_geom)
    nodes_gdf.crs = CRS.from_epsg(4326)  # Assuming latitude/longitude coordinates
    nodes_gdf.to_file(nodes_file)

    # Edges
    edge_geom = [LineString([Point(G.nodes[u]['x'], G.nodes[u]['y']), Point(G.nodes[v]['x'], G.nodes[v]['y'])]) for u, v in G.edges()]
    edges_gdf = gpd.GeoDataFrame({'source': [u for u, v in G.edges()], 'target': [v for u, v in G.edges()]}, geometry=edge_geom)
    edges_gdf.crs = CRS.from_epsg(4326)  # Assuming latitude/longitude coordinates
    edges_gdf.to_file(edges_file)

# Create a networkx DiGraph (directed graph)
G = nx.DiGraph()

# Add nodes with WKT keys
G.add_nodes_from([(1, {'x': 0, 'y': 0}), (2, {'x': 1, 'y': 1}), (3, {'x': 2, 'y': 0})])

# Add edges
G.add_edges_from([(1, 2), (2, 3)])

# Write to shapefiles
write_to_shapefiles(G, 'nodes.shp', 'edges.shp')
