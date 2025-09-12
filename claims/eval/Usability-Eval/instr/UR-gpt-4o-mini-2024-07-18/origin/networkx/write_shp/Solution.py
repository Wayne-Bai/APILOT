import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString

def write_graph_to_shapefiles(graph, nodes_file, edges_file):
    # Prepare node geometries
    nodes_data = []
    for node, data in graph.nodes(data=True):
        if 'Wkb' in data:
            geometry = Point(data['Wkb'])  # Assuming Wkb is a tuple (x, y)
        elif 'Wkt' in data:
            geometry = Point(data['Wkt'])  # Assuming Wkt is a valid WKT for Point
        elif isinstance(node, tuple) and len(node) == 2:  # Numeric tuple (x, y)
            geometry = Point(node)
        else:
            continue
        nodes_data.append({'geometry': geometry, 'properties': data})

    # Create GeoDataFrame for nodes
    nodes_gdf = gpd.GeoDataFrame(nodes_data)

    # Write nodes to shapefile
    nodes_gdf.to_file(nodes_file, driver='ESRI Shapefile')

    # Prepare edge geometries
    edges_data = []
    for u, v, data in graph.edges(data=True):
        if 'Wkb' in data:
            geometry = LineString([Point(data['Wkb'][u]), Point(data['Wkb'][v])])
        elif 'Wkt' in data:
            geometry = LineString([Point(data['Wkt'][u]), Point(data['Wkt'][v])])
        else:
            continue
        edges_data.append({'geometry': geometry, 'properties': data})

    # Create GeoDataFrame for edges
    edges_gdf = gpd.GeoDataFrame(edges_data)

    # Write edges to shapefile
    edges_gdf.to_file(edges_file, driver='ESRI Shapefile')

# Example usage:
# Creating a directed graph
G = nx.DiGraph()
G.add_node((1, 2), Wkb=(1, 2), attr1='node1')
G.add_node((3, 4), Wkt='POINT (3 4)', attr2='node2')
G.add_edge((1, 2), (3, 4), Wkb={((1, 2)): (3, 4)}, attr='edge1')

# Writing to shapefiles
write_graph_to_shapefiles(G, 'nodes.shp', 'edges.shp')
