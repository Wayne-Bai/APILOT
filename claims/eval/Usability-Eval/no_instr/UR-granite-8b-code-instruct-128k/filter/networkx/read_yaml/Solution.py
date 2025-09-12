import networkx as nx
import yaml

def read_graph_yaml(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    G = nx.Graph()
    for node in data['nodes']:
        G.add_node(node['id'])

    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'])

    return G
