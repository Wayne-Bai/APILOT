import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString

# Sample DiGraph creation
G = nx.DiGraph()

# Add nodes with WKT or numeric tuple (x, y)
G.add_node(1, wkt='POINT(1 1)')
G.add_node(2, x=2, y=2)

# Add edges with WKT
G.add_edge(1, 2, wkt='LINESTRING(1 1, 2 2)')

# Function to convert WKT to geometry
def wkt_to_geometry(wkt):
    return gpd.GeoSeries.from_wkt([wkt]).iloc[0]

# Function to convert numeric tuple to Point
def tuple_to_point(coords):
    return Point(coords)

# Create GeoDataFrames for nodes and edges
node_gdf = gpd.GeoDataFrame(columns=['geometry'])
edge_gdf = gpd.GeoDataFrame(columns=['geometry'])

# Populate node GeoDataFrame
for node, data in G.nodes(data=True):
    if 'wkt' in data:
        geometry = wkt_to_geometry(data['wkt'])
    elif 'x' in data and 'y' in data:
        geometry = tuple_to_point((data['x'], data['y']))
    else:
        continue
    node_gdf = node_gdf.append({'geometry': geometry}, ignore_index=True)

# Populate edge GeoDataFrame
for u, v, data in G.edges(data=True):
    if 'wkt' in data:
        geometry = wkt_to_geometry(data['wkt'])
    else:
        continue
    edge_gdf = edge_gdf.append({'geometry': geometry}, ignore_index=True)

# Write to shapefiles
node_gdf.to_file('nodes.shp', driver='ESRI Shapefile')
edge_gdf.to_file('edges.shp', driver='ESRI Shapefile')
