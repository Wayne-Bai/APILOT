import networkx as nx
from shapely.geometry import Point, LineString
from fiona import collection

def shapefile_to_networkx(filename):
    """
    Generate a networkx.DiGraph from shapefiles. Point geometries are translated
    into nodes, lines into edges. Coordinate tuples are used as keys. Attributes
    are preserved, line geometries are simplified into start and end coordinates.

    Parameters
    ----------
    filename : string
        The name of the shapefile or the directory containing many shapefiles.

    Returns
    -------
    G : networkx.DiGraph
    """
    G = nx.DiGraph()

    if not filename.endswith('.shp'):
        filename = os.path.join(filename, '*.shp')

    with collection(filename, "r") as input:
        for shape in input:
            if shape['geometry']['type'] == 'Point':
                G.add_node(shape['geometry']['coordinates'], **shape['properties'])
            elif shape['geometry']['type'] == 'LineString':
                line = LineString(shape['geometry']['coordinates'])
                G.add_edge(line.coords[0], line.coords[-1], **shape['properties'])

    return G
