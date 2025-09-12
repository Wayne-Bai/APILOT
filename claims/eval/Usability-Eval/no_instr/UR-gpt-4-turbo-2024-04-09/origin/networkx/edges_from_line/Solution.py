import networkx as nx

def create_edges_from_geom(geom):
    edges = [(line.coords[0], line.coords[-1]) for line in geom]
    return edges

# Example usage within a context of reading shapefiles
def read_shp(shapefile_path):
    import geopandas as gpd
    gdf = gpd.read_file(shapefile_path)
    
    # Assuming 'geometry' column contains line geometries
    geom = gdf['geometry']
    edges = create_edges_from_geom(geom)
    
    G = nx.Graph()
    G.add_edges_from(edges)
    return G
