import networkx as nx
import geopandas as gpd
from shapely.wkt import loads
from shapely.geometry import Point, LineString

# Sample DiGraph creation
G = nx.DiGraph()
G.add_node(1, Wkt='POINT(1 1)')
G.add_node(2, Wkt='POINT(2 2)')
G.add_edge(1, 2, Wkt='LINESTRING(1 1, 2 2)')

# Function to convert Wkt to geometry
def wkt_to_geometry(wkt_str):
    return loads(wkt_str)

# Create GeoDataFrame for nodes
node_gdf = gpd.GeoDataFrame(columns=['geometry'])
for node, data in G.nodes(data=True):
    if 'Wkt' in data:
        geometry = wkt_to_geometry(data['Wkt'])
    elif isinstance(node, tuple) and len(node) == 2:
        geometry = Point(node)
    else:
        raise ValueError(f"Node {node} does not have a valid geometry representation.")
    node_gdf = node_gdf.append({'geometry': geometry}, ignore_index=True)

# Create GeoDataFrame for edges
edge_gdf = gpd.GeoDataFrame(columns=['geometry'])
for u, v, data in G.edges(data=True):
    if 'Wkt' in data:
        geometry = wkt_to_geometry(data['Wkt'])
    else:
        raise ValueError(f"Edge ({u}, {v}) does not have a valid geometry representation.")
    edge_gdf = edge_gdf.append({'geometry': geometry}, ignore_index=True)

# Save to shapefiles
node_gdf.to_file('nodes.shp', driver='ESRI Shapefile')
edge_gdf.to_file('edges.shp', driver='ESRI Shapefile')
