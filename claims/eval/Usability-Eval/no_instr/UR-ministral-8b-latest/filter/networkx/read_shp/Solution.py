import networkx as nx
from shapely.geometry import Point, LineString
from shapely.wkb import loads
import fiona
from shapely.geometry import shape

def shapefile_to_digraph(shapefile_path):
    G = nx.DiGraph()

    if shapefile_path.endswith('.shp'):
        with fiona.open(shapefile_path, 'r') as source:
            for feat in source:
                geometry = shape(feat['geometry'])
                if isinstance(geometry, Point):
                    G.add_node(geometry.yx, type="point", attributes=feat['properties'])
                elif isinstance(geometry, LineString):
                    edges = solve_line(geometry.coords)
                    for edge in edges:
                        G.add_edge(edge[0], edge[1], type="line", attributes=feat['properties'])
    elif shapefile_path.endswith('/'):
        for file in fiona.directory_iterator(shapefile_path):
            G = G.copy()
            with fiona.open(file, 'r') as src:
                for feat in src:
                    geometry = shape(feat['geometry'])
                    if isinstance(geometry, Point):
                        G.add_node(geometry.yx, type="point", attributes=feat['properties'])
                    elif isinstance(geometry, LineString):
                        edges = solve_line(geometry.coords)
                        for edge in edges:
                            G.add_edge(edge[0], edge[1], type="line", attributes=feat['properties'])
    else:
        raise ValueError("The provided path is not a valid shapefile or directory.")

    return G

def solve_line(line_coords):
    edges = []
    for i in range(len(line_coords)-1):
        edges.append([(line_coords[i], line_coords[i+1])])
    return edges
