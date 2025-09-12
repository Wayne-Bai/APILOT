
import networkx as nx
import yaml

G = nx.Graph([(1, 2), (2, 3), (3, 4)])

with open('graph.yaml', 'w') as f:
    yaml.dump(nx.readwrite.nx_yaml.write_yaml(G), f)
