import networkx as nx
from shapely.geometry import Point

# Assuming G is your networkx.DiGraph and nodes and edges are defined

# Function to create points from nodes with x,y coordinates
def create_points_from_nodes(G):
    nodes_with_coords = {node: Point(x, y) for node, x, y in zip(G.nodes(), G.nodes().data('x'), G.nodes().data('y'))}
    return nodes_with_coords

# Function to write nodes to shapefile
def write_nodes_to_shapefile(nodes, filename):
    with open(filename, 'w') as f:
        f.write('<FeatureCollection>\n  <FeatureCollection type="FeatureCollection">\n')
        for node, geom in nodes.items():
            f.write(f'    <Feature id="{node}" geometry="{geom.wkt}" />\n')
        f.write('  </FeatureCollection>\n</FeatureCollection>\n')

# Function to write edges to shapefile
def write_edges_to_shapefile(edges, filename):
    with open(filename, 'w') as f:
        f.write('<FeatureCollection>\n  <FeatureCollection type="FeatureCollection">\n')
        for edge, geom in edges.items():
            f.write(f'    <Feature id="{edge}" geometry="{geom.wkb}" />\n')
        f.write('  </FeatureCollection>\n</FeatureCollection>\n')

# Create points from nodes
nodes_with_coords = create_points_from_nodes(G)

# Write nodes to shapefile
write_nodes_to_shapefile(nodes_with_coords, 'nodes.shp')

# Create edges from edges
edges_with_geoms = create_points_from_nodes(G)

# Write edges to shapefile
write_edges_to_shapefile(edges_with_geoms, 'edges.shp')
