import networkx as nx

def generate_graph(graph_description):
    G = nx.Graph()

    # Create nodes
    nodes = list(map(int, graph_description.split()))
    G.add_nodes_from(nodes)

    # Create edges
    edges = graph_description.split(';')
    for edge in edges:
        node1, node2 = map(int, edge.split(':'))
        G.add_edge(node1, node2)

    return G
