import networkx as nx
import shapefile

def read_shp(shp_path):
    G = nx.Graph()
    sf = shapefile.Reader(shp_path)
    
    for shape_rec in sf.shapeRecords():
        geom = shape_rec.shape.points
        for i in range(len(geom) - 1):
            G.add_edge(tuple(geom[i]), tuple(geom[i + 1]))
    
    return G
