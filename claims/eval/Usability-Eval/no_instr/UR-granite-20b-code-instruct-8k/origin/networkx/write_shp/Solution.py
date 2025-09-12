import networkx as nx
from shapely.geometry import shape, Point
import fiona

def write_graph_to_shapefiles(graph, edge_filename, node_filename):
    # Write edges to a shapefile
    with fiona.open(edge_filename, 'w', schema={'geometry': fiona. geometry.LineString(), 'properties': {'id': 'int'}}, crs={'init': 'epsg:4326'}, driver='ESRI Shapefile') as c:
        for i, (u, v, data) in enumerate(graph.edges(data=True)):
            c.write({'geometry': shape(data['geometry']), 'properties': {'id': i}})

    # Write nodes to a shapefile
    with fiona.open(node_filename, 'w', schema={'geometry': fiona.geometry.Point(), 'properties': {'id': 'int'}}, crs={'init': 'epsg:4326'}, driver='ESRI Shapefile') as c:
        for i, (node, data) in enumerate(graph.nodes(data=True)):
            if 'geometry' in data:
                c.write({'geometry': shape(data['geometry']), 'properties': {'id': i}})
            elif 'x' in data and 'y' in data:
                c.write({'geometry': Point(data['x'], data['y']), 'properties': {'id': i}})
