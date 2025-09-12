import networkx as nx

# Load the shapefiles
G = nx.read_shp('path/to/shapefiles')

# Simplify line geometries
for u, v, data in G.edges(data=True):
    if 'geometry' in data:
        data['geometry'] = data['geometry'].simplify(0.0001)

# Add start and end coordinates as attributes
for u, v, data in G.edges(data=True):
    if 'geometry' in data:
        start_x, start_y = data['geometry'].coords[0]
        end_x, end_y = data['geometry'].coords[-1]
        data['start_x'] = start_x
        data['start_y'] = start_y
        data['end_x'] = end_x
        data['end_y'] = end_y

print(G)
