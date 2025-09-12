import networkx as nx

def read_yaml_graph(path):
    graph = nx.read_yaml(path)
    return graph
