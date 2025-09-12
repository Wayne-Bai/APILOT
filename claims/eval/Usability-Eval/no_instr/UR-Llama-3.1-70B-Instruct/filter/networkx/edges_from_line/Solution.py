import networkx as nx
import numpy as np

def add_line_edges(G, geom, attr=None):
    """
    Generate edges for each line in geom and add them to the graph G.
    
    Parameters
    ----------
    G : networkx.Graph
        The graph to which the edges will be added.
    geom : list of lists of tuples
        A list of lines where each line is a list of (x, y) coordinates.
    attr : dict (optional)
        Attributes to be assigned to each edge.
        
    Returns
    -------
    G : networkx.Graph
        The graph with the added edges.
    """
    for line in geom:
        for i in range(len(line) - 1):
            node1 = line[i]
            node2 = line[i + 1]
            if attr:
                G.add_edge(node1, node2, **attr)
            else:
                G.add_edge(node1, node2)
    return G


def read_shp(filename):
    """
    Read a shapefile and return the graph.
    
    Parameters
    ----------
    filename : str
        The path to the shapefile.
        
    Returns
    -------
    G : networkx.Graph
        The graph representing the shapefile.
    """
    # Use a library like Fiona to read the shapefile
    import fiona
    with fiona.open(filename, 'r') as src:
        crs = src.crs
        geom = [feature['geometry']['coordinates'] for feature in src]
        G = nx.Graph()
        G = add_line_edges(G, geom)
        return G


# Example usage
G = read_shp('path_to_your_shapefile.shp')
print(nx.edges(G))
