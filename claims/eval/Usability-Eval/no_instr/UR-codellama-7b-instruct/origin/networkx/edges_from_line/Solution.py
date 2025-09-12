
import networkx as nx

def generate_edges(geom):
    """Generate edges for each line in geom."""
    edges = []
    for line in geom:
        x, y = line.xy
        edges.append(((x[0], y[0]), (x[1], y[1])))
    return edges
