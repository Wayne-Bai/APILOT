import networkx as nx

def generate_edges(geom):
    G = nx.Graph()
    for line in geom:
        # Assuming line is a shapely LineString object
        # You may need to adjust the following line based on your actual data
        G.add_edge(line.coords[0], line.coords[-1])
    return G
