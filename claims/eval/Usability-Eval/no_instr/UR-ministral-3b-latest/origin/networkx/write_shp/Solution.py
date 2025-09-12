import networkx as nx
from shapely.geometry import Point, MultiPoint
import fiona
import geopandas as gpd

# Create a sample graph
G = nx.DiGraph()
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 5, weight=2)

# Add nodes with wkb/wkt keys
G.add_node(1, wkt="POINT(1 1)")
G.add_node(2, wkt="POINT(2 2)")
G.add_node(3, wkt="POINT(3 3)")
G.add_node(4, wkt="POINT(4 4)")
G.add_node(5, wkt="POINT(5 5)")

# Write nodes to shapefile
nodes = []
for n, w in G.nodes(data=True):
    if isinstance(w.get('wkt'), str):
        geom = gpd.read_file(w).geometry.values[0]
    elif isinstance(w.get('wkb'), bytes):
        geom = gpd.read_file(fiona.open({}, 'rb+'), 'w').geometry.values[0]
    else:
        geom = Point(w)

    nodes.append((n, geom.wkt))

gdf_nodes = gpd.DataFrame(nodes, columns=['id', 'wkt'])
gdf_nodes.to_file('nodes.shp')

# Write edges to shapefile
edges = []
for u, v in G.edges(data=True):
    geom = MultiPoint([
        Point(G.nodes[u]['wkt']),
        Point(G.nodes[v]['wkt'])
    ]).convex_hull

    edges.append((u, v, geom.wkt))

gdf_edges = gpd.DataFrame(edges, columns=['u', 'v', 'wkt'])
gdf_edges.to_file('edges.shp')
