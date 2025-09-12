import networkx as nx
from shapely.geometry import Point, LineString
import os
from shapely.io import shapeparser

def generate_graph(shapefile_or_dir):
    G = nx.DiGraph()

    if os.path.isdir(shapefile_or_dir):
        for filename in os.listdir(shapefile_or_dir):
            if filename.endswith(".shp"):
                with shapeparser.Shape(shapefile_or_dir + "/" + filename) as shape:
                    for record in shape:
                        geom = record.geometry
                        if geom.geom_type == "Point":
                            G.add_node(geom.coords[0], **record.attributes)
                        elif geom.geom_type == "LineString":
                            start = geom.coords[0]
                            end = geom.coords[-1]
                            G.add_edge(start, end, **record.attributes)
    else:
        with shapeparser.Shape(shapefile_or_dir) as shape:
            for record in shape:
                geom = record.geometry
                if geom.geom_type == "Point":
                    G.add_node(geom.coords[0], **record.attributes)
                elif geom.geom_type == "LineString":
                    start = geom.coords[0]
                    end = geom.coords[-1]
                    G.add_edge(start, end, **record.attributes)

    return G
