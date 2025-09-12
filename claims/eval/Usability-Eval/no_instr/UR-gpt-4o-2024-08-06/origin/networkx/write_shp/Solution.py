import networkx as nx
from shapely.wkt import loads as load_wkt
from shapely.wkb import loads as load_wkb
from shapely.geometry import Point, LineString, mapping
import fiona
from fiona.crs import from_epsg

def graph_to_shapefiles(G, node_shapefile='nodes.shp', edge_shapefile='edges.shp', crs_epsg=4326):
    # Define schema for nodes shapefile
    node_schema = {
        'geometry': 'Point',
        'properties': {key: 'str' for key in G.nodes[next(iter(G.nodes()))].keys()}
    }
    
    # Define schema for edges shapefile
    edge_schema = {
        'geometry': 'LineString',
        'properties': {key: 'str' for key in G.edges[next(iter(G.edges()))].keys()}
    }
    
    # Write nodes to shapefile
    with fiona.open(node_shapefile, 'w', driver='ESRI Shapefile',
                    crs=from_epsg(crs_epsg), schema=node_schema) as node_file:
        for node, data in G.nodes(data=True):
            geom = None
            if 'Wkt' in data:
                geom = load_wkt(data['Wkt'])
            elif 'Wkb' in data:
                geom = load_wkb(data['Wkb'])
            elif isinstance(node, tuple) and len(node) == 2 and all(isinstance(coord, (int, float)) for coord in node):
                geom = Point(node)
            
            if geom:
                node_file.write({
                    'geometry': mapping(geom),
                    'properties': {key: str(data[key]) for key in data}
                })
    
    # Write edges to shapefile
    with fiona.open(edge_shapefile, 'w', driver='ESRI Shapefile',
                    crs=from_epsg(crs_epsg), schema=edge_schema) as edge_file:
        for start, end, data in G.edges(data=True):
            geom = None
            start_node_data = G.nodes[start]
            end_node_data = G.nodes[end]
            if 'Wkt' in data:
                geom = load_wkt(data['Wkt'])
            elif 'Wkb' in data:
                geom = load_wkb(data['Wkb'])
            elif all(isinstance(coord, (int, float)) for coord in start) and all(isinstance(coord, (int, float)) for coord in end):
                if isinstance(start, tuple) and isinstance(end, tuple):
                    geom = LineString([start, end])
            
            if geom:
                edge_file.write({
                    'geometry': mapping(geom),
                    'properties': {key: str(data[key]) for key in data}
                })

# Example usage
G = nx.DiGraph()
G.add_node((1, 2), Wkt='POINT(1 2)', name='A')
G.add_node((2, 3), Wkt='POINT(2 3)', name='B')
G.add_edge((1, 2), (2, 3), Wkt='LINESTRING(1 2, 2 3)', weight=1.0)

graph_to_shapefiles(G)
