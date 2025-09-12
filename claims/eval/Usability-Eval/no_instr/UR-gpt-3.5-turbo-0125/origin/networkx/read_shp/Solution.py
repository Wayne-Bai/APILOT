
import os
import shapefile
import networkx as nx

def create_digraph_from_shapefiles(shapefiles_path):
    G = nx.DiGraph()

    def add_node(point):
        G.add_node(point, geometry=point)

    def add_edge(edge):
        start, end = edge
        G.add_edge(start, end, geometry=[start, end])

    def process_shapefile(sf):
        for shape in sf.shapes():
            if shape.shapeType == shapefile.POINT:
                point = tuple(shape.points[0])
                add_node(point)
            elif shape.shapeType == shapefile.POLYLINE:
                points = shape.points
                if len(points) >= 2:
                    edge = (tuple(points[0]), tuple(points[-1]))
                    add_edge(edge)

    if os.path.isdir(shapefiles_path):
        for filename in os.listdir(shapefiles_path):
            if filename.endswith(".shp"):
                sf = shapefile.Reader(os.path.join(shapefiles_path, filename))
                process_shapefile(sf)
    elif os.path.isfile(shapefiles_path):
        sf = shapefile.Reader(shapefiles_path)
        process_shapefile(sf)

    return G

path_to_shapefiles = "path/to/shapefiles"
G = create_digraph_from_shapefiles(path_to_shapefiles)
print(G.nodes(data=True))
print(G.edges(data=True))
