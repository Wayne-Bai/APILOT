import networkx as nx
import yaml

def write_graph_to_yaml(graph, path):
    yaml.dump(graph, open(path, "w"))

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)

write_graph_to_yaml(G, "graph.yaml")
