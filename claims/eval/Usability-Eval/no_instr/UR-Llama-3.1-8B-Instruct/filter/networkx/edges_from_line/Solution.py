import networkx as nx
import geopandas as gpd
import shapely.geometry as sg


def generate_edgers_for_shp_helper(shp_file):
    # Read the shapefile
    geom_gdf = gpd.read_file(shp_file)

    # Initialize an empty graph
    graph = nx.Graph()

    # Get the geometries of the shapefile
    geometries = geom_gdf.geometry

    for i in range(0, len(geometries)):
        for j in range(i + 1, len(geometries)):
            # Check if geometries intersect
            if geometries[i].intersects(geometries[j]):
                # Add edge between the two geometries
                graph.add_edge(f'Geometry_{i}', f'Geometry_{j}')

    return graph


# Example usage
shp_file = 'your_shp_file.shp'
graph = generate_edgers_for_shp_helper(shp_file)

print(graph.edges)
