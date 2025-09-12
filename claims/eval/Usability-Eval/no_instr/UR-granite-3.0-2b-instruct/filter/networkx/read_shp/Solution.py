import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import simplify

def shapefile_to_digraph(shapefile_path):
    G = nx.DiGraph()

    # Read shapefile
    gdf = gpd.read_file(shapefile_path)

    # Iterate over geometries
    for index, row in gdf.iterrows():
        geometry = row['geometry']
        x, y = geometry.x, geometry.y
        coord = (x, y)

        # Add node if geometry is a point
        if geometry.geometry_type == 'Point':
            G.add_node(coord, attr=row.attrs)
        # Add edge if geometry is a line
        elif geometry.geometry_type == 'LineString':
            G.add_edge(coord, simplify(geometry).coords[0])

    return G
