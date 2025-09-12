import networkx as nx
from shapely import geometry

def read_shp(file_path):
    # Simulating the reading of a shapefile; actual function may vary
    import fiona
    dataset = fiona.open(file_path, 'r')
    geom_list = [feature['geometry'] for feature in dataset]
    dataset.close()
    return geom_list

def generate_edges(geom):

    G = nx.Graph()

    for line in geom:
        shape = geometry.LineString(line.Coordinates)
        coordinates = list(shape.coords[:-1])  # Last coordinate is the repeated starting point

        for i in range(len(coordinates) - 1):
            u, v = coordinates[i], coordinates[i + 1]
            G.add_edge(u, v)

    return G

# Example usage
file_path = 'path_to_your_shapefile.shp'
geom_list = read_shp(file_path)
G = generate_edges(geom_list)

# For demonstration, print the edges
for edge in G.edges:
    print(edge)
