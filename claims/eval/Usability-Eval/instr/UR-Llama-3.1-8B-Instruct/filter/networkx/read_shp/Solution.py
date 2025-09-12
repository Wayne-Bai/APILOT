import networkx as nx
import fiona
import shapely.geometry as sg
import os

def shape2net(shapefile, simplify=True, dir=False):
    """
    Generate a DiGraph from shapefile(s).
    
    Parameters
    ----------
    shapefile : str
        Path to shapefile(s), or a directory containing many shapefiles.
    simplify : bool (default=True)
        Simplify line geometries into start and end coordinates.
    dir : bool (default=False)
        Consider all.shp files in the given directory as shapefiles.
    
    Returns
    -------
    G : DiGraph
        A directed graph where point geometries are translated into nodes,
        and line geometries into edges.
    """
    
    # Create a new Directed Graph
    G = nx.DiGraph()
    
    # Check if shapefile or a directory is given
    if dir:
        shapefiles = os.listdir(shapefile)
    else:
        shapefiles = [shapefile]
    
    for shp in shapefiles:
        if shp.endswith('.shp'):
            # Read shapefile
            with fiona.open(shapefile + '/' + shp) as src:
                for feature in src:
                    geom = sg.shape(feature['geometry'])
                    
                    # Add point geometries to graph nodes
                    if geom.geom_type == 'Point':
                        G.add_node(tuple(geom.coords[0]), **feature['properties'])
                    # Add line geometries to graph edges
                    elif geom.geom_type == 'LineString':
                        if simplify:
                            start_point = geom.coords[0]
                            end_point = geom.coords[-1]
                            G.add_edge(tuple(start_point), tuple(end_point), key=str(shp) + '->' + str(style(feature['geometry']['geometry_type'])) + str(feature['properties']))
                        else:
                            G.add_edges_from([(tuple(c), tuple(c)) for c in geom.coords], key=str(shp) + '->' + str(style(feature['geometry']['geometry_type'])) + str(feature['properties']))
    
    return G

def style(geom):
    return geom.split('.')[-1].replace("'","")

if __name__ == "__main__":
    # Replace 'path_to_shapefile' with your actual local file path.
    shape2net('path_to_shapefile', simplify=True, dir=True)
