import networkx as nx
import yaml

def read_graph_yaml(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)

    graph = nx.Graph()
    for node, node_data in data['nodes'].items():
        graph.add_node(node, **node_data)
    for edge in data['edges']:
        graph.add_edge(*edge)

    return graph
