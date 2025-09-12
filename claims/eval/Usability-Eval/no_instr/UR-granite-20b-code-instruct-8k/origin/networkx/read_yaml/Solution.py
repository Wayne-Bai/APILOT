import networkx as nx
import yaml

def read_yaml_graph(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    graph = nx.Graph()
    for edge in data['edges']:
        graph.add_edge(edge[0], edge[1])

    return graph
