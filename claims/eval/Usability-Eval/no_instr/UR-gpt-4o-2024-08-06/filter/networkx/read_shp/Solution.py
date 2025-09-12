import os
import networkx as nx
import shapefile

def generate_digraph_from_shapefiles(shapefile_path):
    G = nx.DiGraph()

    def process_shapefile(shp_reader):
        for shape_rec in shp_reader.iterShapeRecords():
            shape = shape_rec.shape
            record = shape_rec.record
            if shape.shapeType in [shapefile.POINT, shapefile.POINTZ, shapefile.POINTM]:
                point = (shape.points[0][0], shape.points[0][1])
                G.add_node(point, **record.as_dict())

            elif shape.shapeType in [shapefile.POLYLINE, shapefile.POLYLINEZ, shapefile.POLYLINEM]:
                for line in shape.parts:
                    start = (shape.points[line][0], shape.points[line][1])
                    if line < len(shape.parts) - 1:
                        end_part = shape.parts[line + 1] - 1
                    else:
                        end_part = len(shape.points) - 1
                    end = (shape.points[end_part][0], shape.points[end_part][1])
                    G.add_edge(start, end, **record.as_dict())

    if os.path.isfile(shapefile_path):
        with shapefile.Reader(shapefile_path) as shp:
            process_shapefile(shp)

    elif os.path.isdir(shapefile_path):
        for filename in os.listdir(shapefile_path):
            if filename.endswith(".shp"):
                with shapefile.Reader(os.path.join(shapefile_path, filename)) as shp:
                    process_shapefile(shp)

    return G

# Example usage:
# graph = generate_digraph_from_shapefiles("path/to/shapefile_or_directory")
