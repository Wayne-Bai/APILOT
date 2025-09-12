import networkx as nx
from shapely.geometry import Point, LineString

def generate_networkx_digraph_from_shapefiles(shapefiles):
    G = nx.DiGraph()
    
    for shapefile in shapefiles:
        with fiona.open(shapefile, 'r') as source:
            for feature in source:
                geometry = shape(feature['geometry'])
                if isinstance(geometry, Point):
                    G.add_node(tuple(geometry.coords[0]), feature['properties'])
                elif isinstance(geometry, LineString):
                    start_coords = tuple(geometry.coords[0])
                    end_coords = tuple(geometry.coords[-1])
                    G.add_edge(start_coords, end_coords, feature['properties'])
    
    return G
