import networkx as nx
from shapely.geometry import LineString

def generate_edges_from_geom(geom):
    edges = []
    for line in geom:
        if isinstance(line, LineString):
            coords = list(line.coords)
            for i in range(len(coords) - 1):
                edges.append((coords[i], coords[i + 1]))
    return edges

# Example usage with read_shp function:
# def read_shp(filepath):
#     # Assuming geom is the geometries read from the shapefile
#     geom = ... # your code to read geometries from shapefile
#     edges = generate_edges_from_geom(geom)
#     return edges
