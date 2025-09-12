import networkx as nx
import os
from osgeo import ogr, osr

def read_shapefile(file_path):
    """Reads a shapefile and returns a networkx.DiGraph"""
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(file_path, 0)  # 0 means read-only.
    layer = dataSource.GetLayer()

    G = nx.DiGraph()
    
    # Get the spatial reference system
    srs = layer.GetSpatialRef()
    srs_auto = osr.SpatialReference()
    srs_auto.ImportFromEPSG(4326)  # Assuming a default output to WGS84

    coord_trans = osr.CoordinateTransformation(srs, srs_auto)

    for feature in layer:
        geom = feature.GetGeometryRef()
        geom_type = geom.GetGeometryType()

        if geom_type == ogr.wkbPoint or geom_type == ogr.wkbPoint25D:
            # Add point as a node
            geom.Transform(coord_trans)
            coord = (geom.GetX(), geom.GetY())
            attrs = feature.items()
            G.add_node(coord, **attrs)
        elif geom_type == ogr.wkbLineString or geom_type == ogr.wkbLineString25D:
            # Add line as an edge with start and end coordinates
            geom.Transform(coord_trans)
            start_coord = (geom.GetPoint(0)[0], geom.GetPoint(0)[1])
            end_coord = (geom.GetPoint(geom.GetPointCount() - 1)[0], geom.GetPoint(geom.GetPointCount() - 1)[1])
            attrs = feature.items()
            G.add_edge(start_coord, end_coord, **attrs)
    
    return G

def generate_network_from_shapefiles(directory):
    """Generates a networkx.DiGraph from shapefiles in a directory or a single shapefile."""
    G = nx.DiGraph()

    if os.path.isfile(directory):
        # It's a single shapefile
        G = nx.compose(G, read_shapefile(directory))
    elif os.path.isdir(directory):
        # It's a directory of shapefiles
        for filename in os.listdir(directory):
            if filename.endswith(".shp"):
                file_path = os.path.join(directory, filename)
                G = nx.compose(G, read_shapefile(file_path))
    
    return G

# Example usage:
# graph = generate_network_from_shapefiles('/path/to/shapefile/or/directory')
