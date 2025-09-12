import networkx as nx
import fiona

def write_networkx_to_shapefiles(G, edges_filename, nodes_filename):
    # Initialize the edges shapefile
    edges_layer = fiona.open(edges_filename, 'w', driver='ESRI Shapefile',
                            crs='EPSG:4326', layer='edges',
                            schema={'geometry': 'LineString', 'properties': {'id': 'int'}})

    # Initialize the nodes shapefile
    nodes_layer = fiona.open(nodes_filename, 'w', driver='ESRI Shapefile',
                            crs='EPSG:4326', layer='nodes',
                            schema={'geometry': 'Point', 'properties': {'id': 'int'}})

    # Add edges to the shapefile
    for u, v, data in G.edges(data=True):
        wkt_edge = fiona.wgbshape([nx.spatial_frontend.shape(u, v)], 'WKT')
        if 'wkb' in data:
            edges_layer.write({'geometry': data['wkb'], 'properties': {'id': u}})
        elif 'wkt' in data:
            edges_layer.write({'geometry': data['wkt'], 'properties': {'id': u}})
        else:
            wkb_edge = fiona.wkbshapes([nx.spatial_frontend.shape(u, v)], 'WKB')
            edges_layer.write({'geometry': wkb_edge, 'properties': {'id': u}})

    # Add nodes to the shapefile
    for i, node in enumerate(G.nodes()):
        if 'wkb' in node:
            nodes_layer.write({'geometry': node['wkb'], 'properties': {'id': i}})
        elif 'wkt' in node:
            nodes_layer.write({'geometry':	node['wkt'], 'properties': {'id': i}})
        elif isinstance(node, tuple):
            nodes_layer.write({'geometry': {'type': 'Point', 'coordinates': node}, 'properties': {'id': i}})
        else:
            nodes_layer.write({'geometry': {'type': 'Point', 'coordinates': (node[0], node[1])}, 'properties': {'id': i}})

    # Close the shapefiles
    edges_layer.close()
    nodes_layer.close()

# Example usage
G = nx.DiGraph()
G.add_node(nx.spatial_frontend.Point(1.5, 2.5), wkt='POINT(1.5 2.5)')
G.add_node(nx.spatial_frontend.Point(2.5, 2.5), wkt='POINT(2.5 2.5)')
G.add_edge(1.5, 2.5, wkt='POINT(1.5 2.5) POINT(2.5 2.5)')

write_networkx_to_shapefiles(G, 'edges.shp', 'nodes.shp')
