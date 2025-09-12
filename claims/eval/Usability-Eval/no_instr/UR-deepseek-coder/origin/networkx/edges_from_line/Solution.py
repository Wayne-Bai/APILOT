import networkx as nx
import shapefile

def read_shp(shp_path):
    G = nx.Graph()
    sf = shapefile.Reader(shp_path)
    shapes = sf.shapes()
    records = sf.records()

    for i, shape in enumerate(shapes):
        geom = shape.points
        for j in range(len(geom) - 1):
            G.add_edge(tuple(geom[j]), tuple(geom[j + 1]))

    return G
