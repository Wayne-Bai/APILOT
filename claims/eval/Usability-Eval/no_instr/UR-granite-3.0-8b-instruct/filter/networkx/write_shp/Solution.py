import networkx as nx
import shapefile

def write_to_shapefiles(G, node_key='Wkb', edge_key='Wkb'):
    """
    Writes a networkx.DiGraph to two shapefiles, edges and nodes.
    Nodes and edges are expected to have a Well Known Binary (Wkb) or Well Known Text (Wkt) key in order to generate geometries.
    Also acceptable are nodes with a numeric tuple key (x,y).

    Parameters:
    G (networkx.DiGraph): The input graph.
    node_key (str): The key for node geometries. Default is 'Wkb'.
    edge_key (str): The key for edge geometries. Default is 'Wkb'.

    Returns:
    None
    """
    # Create shapefiles for nodes and edges
    sf_nodes = shapefile.Writer(shapefile.POINT)
    sf_nodes.field(node_key, 'C')

    sf_edges = shapefile.Writer(shapefile.POLYLINE)
    sf_edges.field(edge_key, 'C')

    # Write nodes to shapefile
    for node, data in G.nodes(data=True):
        if node_key in data:
            sf_nodes.node(node, data[node_key])
        else:
            sf_nodes.node(node, (data['x'], data['y']))

    # Write edges to shapefile
    for u, v, data in G.edges(data=True):
        if edge_key in data:
            sf_edges.line(data[edge_key])
        else:
            sf_edges.line([(data['x1'], data['y1']), (data['x2'], data['y2'])])

    # Save shapefiles
    sf_nodes.save('nodes.shp')
    sf_edges.save('edges.shp')
