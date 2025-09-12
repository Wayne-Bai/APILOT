import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString

def write_graph_to_shapefiles(graph, nodes_shapefile, edges_shapefile):
    # Prepare the nodes data
    nodes_data = {
        'geometry': [Point(graph.nodes[node]['geometry']) if 'geometry' in graph.nodes[node]
                     else Point(graph.nodes[node]['x'], graph.nodes[node]['y'])
                     for node in graph.nodes()],
        'id': list(graph.nodes())
    }
    
    nodes_gdf = gpd.GeoDataFrame(nodes_data, crs="EPSG:4326")  # Define the coordinate reference system
    nodes_gdf.to_file(nodes_shapefile, driver='ESRI Shapefile')
    
    # Prepare the edges data
    edges_data = {
        'geometry': [LineString([graph.nodes[edge[0]]['geometry'], graph.nodes[edge[1]]['geometry']])
                     for edge in graph.edges()],
        'from_node': [edge[0] for edge in graph.edges()],
        'to_node': [edge[1] for edge in graph.edges()]
    }
    
    edges_gdf = gpd.GeoDataFrame(edges_data, crs="EPSG:4326")  # Define the coordinate reference system
    edges_gdf.to_file(edges_shapefile, driver='ESRI Shapefile')

# Example usage
if __name__ == "__main__":
    # Create a directed graph
    G = nx.DiGraph()
    G.add_node(1, geometry=(1.0, 1.0))
    G.add_node(2, geometry=(2.0, 2.0))
    G.add_edge(1, 2)

    # Write to shapefiles
    write_graph_to_shapefiles(G, 'nodes.shp', 'edges.shp')
