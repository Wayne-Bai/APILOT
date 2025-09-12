import networkx as nx
import geopandas as gpd
from shapely.geometry import LineString

def edges_from_lines(geoms):
    """
    Generate edges from LineString geometries.

    Parameters
    ----------
    geoms : iterable of LineString
        Iterable containing LineString geometries.

    Returns
    -------
    edges : list of tuples
        Generated edges as tuples (u, v).
    """

    edges = []
    for geom in geoms:
        if isinstance(geom, LineString):
            coords = list(geom.coords)
            for i in range(len(coords) - 1):
                u = coords[i]
                v = coords[i + 1]
                edges.append((u, v))
    return edges

def read_shapefile_lines(filename):
    """
    Read a shapefile and extract LineString geometries to generate edges.

    Parameters
    ----------
    filename : str
        Path to the shapefile.

    Returns
    -------
    edges : list of tuples
        Edges extracted from LineString geometries in the shapefile.
    """
    
    gdf = gpd.read_file(filename)
    # Extract LineString geometries
    line_geoms = gdf.geometry[gdf.geometry.type == 'LineString']
    return edges_from_lines(line_geoms)

# Example usage:
# edges = read_shapefile_lines('path_to_shapefile.shp')
# G = nx.Graph()
# G.add_edges_from(edges)
