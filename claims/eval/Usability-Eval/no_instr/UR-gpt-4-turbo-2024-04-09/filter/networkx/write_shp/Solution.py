import networkx as nx
from osgeo import ogr, osr

def save_graph_to_shapefiles(G, node_shp_file, edge_shp_file):
    # Create a spatial reference
    spatial_reference = osr.SpatialReference()
    spatial_reference.ImportFromEPSG(4326)  # WGS84

    # Create Node Shapefile
    driver = ogr.GetDriverByName('Esri Shapefile')
    ds = driver.CreateDataSource(node_shp_file)
    layer = ds.CreateLayer('nodes', spatial_reference, ogr.wkbPoint)
    layer.CreateField(ogr.FieldDefn('id', ogr.OFTInteger))
    
    for node, data in G.nodes(data=True):
        feature = ogr.Feature(layer.GetLayerDefn())
        feature.SetField('id', node)
        
        # Check for WKT or Tuple
        if 'Wkt' in data:
            point = ogr.CreateGeometryFromWkt(data['Wkt'])
        elif isinstance(node, tuple) and len(node) == 2 and all(isinstance(coord, (int, float)) for coord in node):
            point = ogr.Geometry(ogr.wkbPoint)
            point.AddPoint(node[0], node[1])
        else:
            continue
        
        feature.SetGeometry(point)
        layer.CreateFeature(feature)
        feature = None
    
    ds = None
    
    # Create Edge Shapefile
    ds = driver.CreateDataSource(edge_shp_file)
    layer = ds.CreateLayer('edges', spatial_reference, ogr.wkbLineString)
    layer.CreateField(ogr.FieldDefn('source', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('target', ogr.OFTInteger))
    
    for source, target, data in G.edges(data=True):
        feature = ogr.Feature(layer.GetLayerDefn())
        feature.SetField('source', source)
        feature.SetField('target', target)
        
        # Check for WKT
        if 'Wkt' in data:
            linestring = ogr.CreateGeometryFromWkt(data['Wkt'])
            feature.SetGeometry(linestring)
        else:
            continue
        
        layer.CreateFeature(feature)
        feature = None
    
    ds = None

# Example of creating and saving a graph
G = nx.DiGraph()
G.add_node(1, Wkt="POINT (10 10)")
G.add_node(2, Wkt="POINT (20 20)")
G.add_edge(1, 2, Wkt="LINESTRING (10 10, 20 20)")

save_graph_to_shapefiles(G, 'nodes.shp', 'edges.shp')
