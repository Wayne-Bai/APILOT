import networkx as nx

def generate_graph(graph_description):
    G = nx.Graph()

    # Create nodes
    nodes = graph_description.split('\n')
    G.add_nodes_from(nodes)

    return G
