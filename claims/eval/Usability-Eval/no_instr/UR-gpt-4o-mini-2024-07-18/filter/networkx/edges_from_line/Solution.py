import networkx as nx
from shapely.geometry import LineString

def generate_edges_from_lines(geom):
    edges = []
    for line in geom:
        if isinstance(line, LineString):
            coords = list(line.coords)
            for i in range(len(coords) - 1):
                edge = (coords[i], coords[i + 1])
                edges.append(edge)
    return edges

def read_shp_and_generate_edges(shapefile_path):
    import geopandas as gpd
    
    gdf = gpd.read_file(shapefile_path)
    all_edges = []
    
    for geometry in gdf.geometry:
        edges = generate_edges_from_lines(geometry)
        all_edges.extend(edges)
    
    return all_edges
