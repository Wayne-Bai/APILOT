
import networkx as nx
import geopandas as gpd

def write_graph_to_shapefiles(G, nodes_filename, edges_filename):
    nodes, edges = G.nodes(data=True), G.edges(data=True)
    
    nodes_df = gpd.GeoDataFrame()
    for node, data in nodes:
        if 'Wkb' in data:
            geom = data['Wkb']
        elif 'Wkt' in data:
            geom = data['Wkt']
        else:
            x, y = node
            geom = Point(x, y)
        nodes_df = nodes_df.append({'ID': node, 'geometry': geom}, ignore_index=True)
    
    nodes_df.to_file(nodes_filename, driver='ESRI Shapefile')
    
    edges_df = gpd.GeoDataFrame()
    for u, v, data in edges:
        if 'Wkb' in data:
            geom = data['Wkb']
        elif 'Wkt' in data:
            geom = data['Wkt']
        edges_df = edges_df.append({'u': u, 'v': v, 'geometry': geom}, ignore_index=True)
    
    edges_df.to_file(edges_filename, driver='ESRI Shapefile')

# Example usage
G = nx.DiGraph()
G.add_node((0, 0), Wkt='POINT (0 0)')
G.add_node((1, 1), Wkb=b'\x00\x01\x02\x03')
G.add_edge((0, 0), (1, 1), Wkt='LINESTRING (0 0, 1 1)')

write_graph_to_shapefiles(G, 'nodes.shp', 'edges.shp')
