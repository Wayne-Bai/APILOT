import networkx as nx
import yaml

# Write a graph to YAML format
def write_graph_yaml(G, filename):
    with open(filename, 'w') as file:
        graph_dict = nx.to_dict_of_lists(G)
        yaml.dump(graph_dict, file)

# Read a graph from YAML format
def read_graph_yaml(filename):
    with open(filename, 'r') as file:
        graph_dict = yaml.safe_load(file)
        G = nx.from_dict_of_lists(graph_dict)
    return G
