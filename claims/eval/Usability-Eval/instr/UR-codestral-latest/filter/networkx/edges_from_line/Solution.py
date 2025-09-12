import networkx as nx

def generate_edges(geom):
    G = nx.Graph()
    for line in geom:
        for i in range(len(line.coords) - 1):
            start = line.coords[i]
            end = line.coords[i + 1]
            G.add_edge(start, end)
    return G

# This function can be used in your read_shp function like this:
# G = generate_edges(geom)
