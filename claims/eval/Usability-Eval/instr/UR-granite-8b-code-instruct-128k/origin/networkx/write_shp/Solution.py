
import networkx as nx
import os
from shapely.wkb import loads

def write_shp(graph, filename):
    nodes = []
    edges = []
    for u, v, data in graph.edges(data=True):
        if 'wkb' in data:
            edges.append({'u': u, 'v': v, 'wkb': data['wkb']})
        elif 'wkt' in data:
            edges.append({'u': u, 'v': v, 'wkt': data['wkt']})
        elif 'x' in data and 'y' in data:
            edges.append({'u': u, 'v': v, 'x': data['x'], 'y': data['y']})
        else:
            raise ValueError('Node or edge data must contain "wkb", "wkt", or "x,y" coordinates')

        nodes.append({'id': u, 'wkb': data['wkb']})
        nodes.append({'id': v, 'wkb': data['wkb']})

    nodes_df = pd.DataFrame(nodes)
    edges_df = pd.DataFrame(edges)

    nodes_df.to_file(filename + '_nodes.shp')
    edges_df.to_file(filename + '_edges.shp')
