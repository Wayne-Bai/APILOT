import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import simplify

def shapefile_to_graph(shapefile_path, attribute_field=None):
    G = nx.DiGraph()

    # Read shapefile
    gdf = gpd.read_file(shapefile_path)

    # Iterate over geometries in the shapefile
    for index, row in gdf.iterrows():
        geometry = row[attribute_field] if attribute_field else row[0]
        x, y = geometry.coords[0]

        # Create node for point geometry
        if geometry.geometry.type == 'Point':
            G.add_node(index, pos=(x, y), attr={attribute_field: row[attribute_field]})

        # Create edge for line geometry
        elif geometry.geometry.type == 'LineString':
            # Simplify line geometry
            simplified_line = simplify(geometry)
            start_point = Point(simplified_line.coords[0])
            end_point = Point(simplified_line.coords[-1])

            # Add edge between start and end points
            G.add_edge(index, index + 1, start_point=start_point, end_point=end_point)

    return G
