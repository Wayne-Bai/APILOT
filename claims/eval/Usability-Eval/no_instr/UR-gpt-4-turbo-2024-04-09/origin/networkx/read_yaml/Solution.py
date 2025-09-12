import networkx as nx
import yaml

def read_graph_from_yaml(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    G = nx.node_link_graph(data)
    return G
