import networkx as nx
import fiona
import shapely
import_shapefile = fiona.collect

def graph_from_shapefile(shapefile):
    G = nx.DiGraph()

    with shapefile as coll:
        for f in coll:
            feature = f['properties']
            geometry = f['geometry']

            if geometry['type'] == 'Point':
                key = tuple(geometry['coordinates'])
                G.add_node(key, **feature)
            elif geometry['type'] == 'LineString':
                start = tuple(geometry['coordinates'][0])
                end = tuple(geometry['coordinates'][-1])
                key = (start, end)
                G.add_edge(start, end, **feature)

    return G

# Usage
graph = graph_from_shapefile('path/to/shapefile.shp')
