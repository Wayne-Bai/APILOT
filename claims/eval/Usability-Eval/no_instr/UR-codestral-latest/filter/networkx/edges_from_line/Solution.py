import networkx as nx

def generate_edges_from_geom(geom):
    edges = []
    for line in geom:
        for i in range(len(line) - 1):
            edges.append((line[i], line[i + 1]))
    return edges

def helper_for_read_shp(shp_path):
    # assuming read_shp function reads shapefile and returns geom data
    geom = read_shp(shp_path)
    edges = generate_edges_from_geom(geom)
    G = nx.Graph()
    G.add_edges_from(edges)
    return G
