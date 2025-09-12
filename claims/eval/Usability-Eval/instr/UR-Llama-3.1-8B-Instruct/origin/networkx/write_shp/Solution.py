import networkx as nx
from shapely.geometry import Point
import fiona
import geopandas as gpd

# Creating a directed graph
G = nx.DiGraph()

# Adding nodes with Well Known Text (Wkt) or numeric tuple keys
G.add_node("A", wkt="POINT (1 2)")
G.add_node("B", wkt="POINT (3 4)")
G.add_node(5, (1, 2))  # node with numeric tuple key

# Adding edges with Wkb key
G.add_edge("A", "B", wkb="LINESTRING (1 2, 3 4)")
G.add_edge(5, "B", wkb="LINESTRING (1 2, 3 4)")

# Converting graph to geospatial data
nodes_gdf = gpd.GeoDataFrame.from_mask(G.nodes(data=True))
edges_gdf = gpd.GeoDataFrame.from_mask(G.edges(data=True, keys=[('u', 'v'), ('u_updatex', 'v_updatex'), ('u_updatey', 'v_updatey'), ('wkb', 'wkt_gdf')]))

# Writing the geospatial dataframes to shapefiles
nodes_gdf.to_file('nodes.shp')
edges_gdf.to_file('edges.shp')
