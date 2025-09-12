import networkx as nx

def write_yaml(G, path):
    with open(path, 'w') as f:
        nx.write_yaml(G, f)
