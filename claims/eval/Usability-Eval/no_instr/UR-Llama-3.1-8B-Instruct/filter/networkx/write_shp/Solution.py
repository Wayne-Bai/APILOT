import networkx as nx
import geopandas as gpd
import fiona
import shapely.geometry as sg

# Create an empty directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_node((0, 0), geometry=sg.Point(0, 0))
G.add_node((1, 1), geometry=sg.Point(1, 1))
G.add_edge(0, 1, {'geometry': sg.LineString([(0, 0), (1, 1)])})

# Convert the graph to a node and edge geodataframe
nodes = nx.get_node_attributes(G, 'geometry')
edges = nx.get_edge_attributes(G, 'geometry')

# Create a geopandas object for the nodes
gdf_nodes = gpd.GeoDataFrame(nodes, geometry='geometry')

# Create a geopandas object for the edges
gdf_edges = gpd.GeoDataFrame(edges, geometry='geometry')

# Make sure the edge geometry CRS matches the node CRS
if gdf_edges.crs is None:
    gdf_edges['geometry'] = gdf_edges['geometry'].apply(lambda x: x.simplify(tolerance=0.1))
if gdf_nodes.crs is None:
    gdf_nodes['geometry'] = gdf_nodes['geometry'].apply(lambda x: x.simplify(tolerance=0.1))

# Convert the geodf to spatialite geometries
gdf_nodes_to_file = gpd.GeoDataFrame(gdf_nodes).to_crs(epsg=4326)
gdf_edges_to_file = gpd.GeoDataFrame(gdf_edges).to_crs(epsg=4326)

# Save to shapefiles
gdf_nodes_to_file.to_file("nodes.shp", driver='ESRI Shapefile')
gdf_edges_to_file.assignPolygonIndex = gdf_edges_to_fileRING_Index = gdf_edges_to_file.sectionIJ_Dim_a = gdf_edges_to_file.nnRequired = gdf_edges_to_file.lineGIS_cNameIndex = gdf_edges_to_fileОР_Fon = None
gdf_edges_to_file.to_file("edges.shp", driver='ESRI Shapefile')
