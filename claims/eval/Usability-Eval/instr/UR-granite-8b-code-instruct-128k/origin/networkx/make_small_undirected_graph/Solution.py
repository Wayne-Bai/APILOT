import networkx as nx

def generate_graph(graph_description):
    graph = nx.Graph()
    for node in graph_description["nodes"]:
        graph.add_node(node)
    for edge in graph_description["edges"]:
        graph.add_edge(edge[0], edge[1])

    return graph
