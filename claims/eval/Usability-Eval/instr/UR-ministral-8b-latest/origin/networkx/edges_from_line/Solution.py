import networkx as nx
import geopandas as gpd
from shapely.geometry import LineString

def read_shp(shp_path):
    gdf = gpd.read_file(shp_path)
    geom = gdf.geometry
    edges = create_edges(geom)
    return edges

def create_edges(geom):
    edges = []
    for line in geom:
        if isinstance(line, LineString):
            line_parts = [(line.x, line.y, line), (line.x + 0.01, line.y, line)]
            edges.extend(line_parts)
    return edges

# Example usage:
# edges = read_shp('path/to/shapefile.shp')
# print(edges)
