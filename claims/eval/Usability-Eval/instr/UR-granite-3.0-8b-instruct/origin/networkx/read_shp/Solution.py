import networkx as nx
import shapefile

def generate_graph(shapefile_or_dir):
    G = nx.DiGraph()

    if isinstance(shapefile_or_dir, str) and shapefile_or_dir.endswith('.shp'):
        sf = shapefile.Reader(shapefile_or_dir)
        for shape in sf.shapes():
            if shape.parts:  # Line or Polygon
                for i in range(len(shape.parts)):
                    start = shape.points[shape.parts[i]][0]
                    end = shape.points[shape.parts[i][-1]]
                    G.add_edge(start, end, **shape.attributes)
            else:  # Point
                G.add_node(shape.points[0], **shape.attributes)
    elif isinstance(shapefile_or_dir, str) and shapefile_or_dir.endswith('.zip'):
        with shapefile.Reader(shapefile_or_dir) as sf:
            for shape in sf.shapes():
                if shape.parts:  # Line or Polygon
                    for i in range(len(shape.parts)):
                        start = shape.points[shape.parts[i]][0]
                        end = shape.points[shape.parts[i][-1]]
                        G.add_edge(start, end, **shape.attributes)
                else:  # Point
                    G.add_node(shape.points[0], **shape.attributes)
    else:
        raise ValueError("Input must be a shapefile or a directory of shapefiles")

    return G
