
import networkx as nx
import geopandas as gpd

def write_shp(G, filename_base):
    # Create a GeoDataFrame for nodes
    node_data = [(node, data) for node, data in G.nodes(data=True)]
    nodes_gdf = gpd.GeoDataFrame(node_data, columns=['id', 'data'])
    
    # Create a GeoDataFrame for edges
    edge_data = []
    for u, v, data in G.edges(data=True):
        edge_data.append((u, v, data))
    edges_gdf = gpd.GeoDataFrame(edge_data, columns=['u', 'v', 'data'])
    
    # Save nodes and edges as shapefiles
    nodes_gdf.to_file(filename_base + '_nodes.shp')
    edges_gdf.to_file(filename_base + '_edges.shp')
