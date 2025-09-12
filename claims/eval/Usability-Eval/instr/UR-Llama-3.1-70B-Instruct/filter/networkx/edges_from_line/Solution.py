import networkx as nx
from shapely.geometry import Polygon, LineString, Point
import matplotlib.pyplot as plt

def geom_edges(geom):
    """
    Generate edges for each line in geom.
    
    Parameters:
    geom (list): A list of LineString objects.
    
    Returns:
    list: A list of edges.
    """
    edges = []
    for line in geom:
        coords = list(line.coords)
        for i in range(len(coords) - 1):
            edges.append((coords[i], coords[i + 1]))
    return edges

# Example usage:
# Create a directed graph
G = nx.DiGraph()

# List of LineString objects
geom = [
    LineString([(0, 0), (1, 1), (2, 2)]),
    LineString([(2, 2), (3, 3), (4, 4)]),
    LineString([(4, 4), (5, 5), (6, 6)])
]

# Generate edges
edges = geom_edges(geom)

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
pos = {x: x for x in G.nodes()}
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue')
plt.show()
