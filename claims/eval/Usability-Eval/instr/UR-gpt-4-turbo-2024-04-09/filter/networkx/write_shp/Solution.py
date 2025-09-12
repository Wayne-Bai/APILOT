import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString

def save_graph_to_shapefile(G, node_shp='nodes.shp', edge_shp='edges.shp'):
    # Extract node and edge data with geometries
    node_data = []
    edge_data = []
    
    for node, data in G.nodes(data=True):
        if 'Wkb' in data:
            geometry = shapely.wkb.loads(data['Wkb'])
        elif 'Wkt' in data:
            geometry = shapely.wkt.loads(data['Wkt'])
        elif isinstance(node, tuple) and len(node) == 2:
            geometry = Point(node[0], node[1])
        else:
            continue  # Skip nodes without recognizable geometric data
        node_data.append({'id': node, 'geometry': geometry, **data})
    
    for u, v, data in G.edges(data=True):
        if 'Wkb' in data:
            geometry = shapely.wkb.loads(data['Wkb'])
        elif 'Wkt' in data:
            geometry = shapely.wkt.loads(data['Wkt'])
        elif isinstance(u, tuple) and isinstance(v, tuple) and len(u) == 2 and len(v) == 2:
            geometry = LineString([Point(u[0], u[1]), Point(v[0], v[1])])
        else:
            continue  # Skip edges without recognizable geometric data
        edge_data.append({'source': u, 'target': v, 'geometry': geometry, **data})

    # Convert to GeoDataFrame
    node_gdf = gpd.GeoDataFrame(node_data)
    edge_gdf = gpd.GeoDataFrame(edge_data)

    # Save to shapefiles
    node_gdf.to_file(node_shp)
    edge_gdf.to_file(edge_shp)

# Example DiGraph
G = nx.DiGraph()
G.add_node((0, 0), Wkt="POINT (0 0)")
G.add_node((1, 1), Wkt="POINT (1 1)")
G.add_edge((0, 0), (1, 1), Wkt="LINESTRING (0 0, 1 1)")

save_graph_to_shapefile(G)
