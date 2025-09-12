import networkx as nx
from shapely.geometry import shape

def edges_from_lines(geom):
    """
    Given a geometric object, extract and generate edges suitable for a graph.
    
    :param geom: A geometric object (Shapely LineString or MultiLineString)
    :return: List of tuples representing edges
    """
    edges = []
    
    # Determine if the geom is a LineString or MultiLineString
    if geom.geom_type == 'LineString':
        coords = list(geom.coords)
        
        # Convert the LineString to a series of edges (tuples)
        edges.extend([(coords[i], coords[i+1]) for i in range(len(coords) - 1)])
    
    elif geom.geom_type == 'MultiLineString':
        for line in geom:
            coords = list(line.coords)
            edges.extend([(coords[i], coords[i+1]) for i in range(len(coords) - 1)])
    
    return edges

def read_shp_edges(geometry_data):
    """
    Processes a list of geometries and returns edges using the edges_from_lines function.
    
    :param geometry_data: List of geometries (such as those from a shapefile)
    :return: List of edges from all geometries
    """
    all_edges = []
    
    for item in geometry_data:
        geom = shape(item)  # Assuming item is in a GeoJSON-like format
        edges = edges_from_lines(geom)
        all_edges.extend(edges)
    
    return all_edges

# Example usage
# Assuming 'geometry_data' is a list of shapely geometry objects.
# geometry_data = [...] 
# edges = read_shp_edges(geometry_data)
# print(edges)
