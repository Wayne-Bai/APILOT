
import networkx as nx
import yaml

def read_graph_from_yaml(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
        G = nx.from_dict_of_lists(data)
    return G

# Example Usage
path = 'example_graph.yaml'
G = read_graph_from_yaml(path)
print(nx.info(G))
