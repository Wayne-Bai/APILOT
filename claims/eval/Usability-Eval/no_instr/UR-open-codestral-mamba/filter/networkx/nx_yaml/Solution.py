
import networkx as nx
import yaml

def save_graph_to_yaml(graph, yaml_file):
    with open(yaml_file, 'w') as outfile:
        yaml.dump(nx.to_dict_of_dicts(graph), outfile)

def load_yaml_to_graph(yaml_file):
    with open(yaml_file, 'r') as infile:
        data = yaml.safe_load(infile)
    G = nx.from_dict_of_dicts(data)
    return G
