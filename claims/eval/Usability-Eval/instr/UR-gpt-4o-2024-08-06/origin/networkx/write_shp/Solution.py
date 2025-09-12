import networkx as nx
import geopandas as gpd
from shapely.wkt import loads as load_wkt
from shapely.geometry import Point, LineString

def graph_to_shapefiles(graph, node_filename, edge_filename):
    # Create a list to store node and edge geometries
    node_geometries = []
    edge_geometries = []

    # Process nodes
    for node, data in graph.nodes(data=True):
        if 'Wkb' in data:
            geometry = load_wkt(data['Wkb'])
        elif 'Wkt' in data:
            geometry = load_wkt(data['Wkt'])
        elif isinstance(node, tuple) and len(node) == 2 and all(isinstance(coord, (int, float)) for coord in node):
            geometry = Point(node)
        else:
            raise ValueError("Node has no valid geometry data: {}".format(node))
        node_geometries.append({'geometry': geometry, **data})

    # Process edges
    for u, v, data in graph.edges(data=True):
        if 'Wkb' in data:
            geometry = load_wkt(data['Wkb'])
        elif 'Wkt' in data:
            geometry = load_wkt(data['Wkt'])
        elif all(isinstance(coord, (int, float)) for edge in [(u, v)] for coord in edge):
            geometry = LineString([Point(u), Point(v)])
        else:
            raise ValueError("Edge has no valid geometry data: {}->{}".format(u, v))
        edge_geometries.append({'geometry': geometry, **data})

    # Create GeoDataFrames
    gdf_nodes = gpd.GeoDataFrame(node_geometries, crs="EPSG:4326")
    gdf_edges = gpd.GeoDataFrame(edge_geometries, crs="EPSG:4326")

    # Write to shapefiles
    gdf_nodes.to_file(node_filename, driver='ESRI Shapefile')
    gdf_edges.to_file(edge_filename, driver='ESRI Shapefile')

# Example usage
G = nx.DiGraph()
G.add_node((1, 2), Wkt="POINT (1 2)")
G.add_node((2, 3), Wkt="POINT (2 3)")
G.add_edge((1, 2), (2, 3), Wkt="LINESTRING (1 2, 2 3)")

graph_to_shapefiles(G, 'nodes.shp', 'edges.shp')
