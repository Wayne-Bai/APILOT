import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, LineString
from pathlib import Path

def shapefile_to_digraph(shapefile_path):
    G = nx.DiGraph()
    
    # Load the shapefile(s)
    if Path(shapefile_path).is_dir():
        gdf = gpd.GeoDataFrame(pd.concat([gpd.read_file(shp) for shp in Path(shapefile_path).glob('*.shp')], ignore_index=True))
    else:
        gdf = gpd.read_file(shapefile_path)
    
    # Process point geometries
    point_geometries = gdf[gdf.geometry.type == 'Point']
    for idx, row in point_geometries.iterrows():
        coords = (row.geometry.x, row.geometry.y)
        G.add_node(coords, **row.drop('geometry').to_dict())
    
    # Process line geometries
    line_geometries = gdf[gdf.geometry.type == 'LineString']
    for idx, row in line_geometries.iterrows():
        line = row.geometry
        start_coords = (line.coords[0][0], line.coords[0][1])
        end_coords = (line.coords[-1][0], line.coords[-1][1])
        G.add_edge(start_coords, end_coords, **row.drop('geometry').to_dict())
    
    return G

# Example usage:
# digraph = shapefile_to_digraph('path_to_shapefile_or_directory')
