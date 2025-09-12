import networkx as nx

def generate_edges_from_geom(geometries):
    """
    Generate edges from geometry lines.
    
    Parameters:
    geometries (list): List of line geometries, each geometry is assumed to be a tuple of points,
                       where each point is a tuple (x, y).

    Returns:
    list: List of edges, where each edge is represented as a tuple ((x1, y1), (x2, y2)).
    """
    G = nx.Graph()
    for geom in geometries:
        # Assume each geom is a list of points forming a polyline
        for start, end in zip(geom[:-1], geom[1:]):
            G.add_edge(start, end)
    
    return list(G.edges())

# Example usage
geometries = [
    [ (0, 0), (1, 1), (2, 2) ],
    [ (2, 2), (3, 3) ],
    [ (0, 0), (0, 1), (0, 2) ]
]

edges = generate_edges_from_geom(geometries)
print(edges)
