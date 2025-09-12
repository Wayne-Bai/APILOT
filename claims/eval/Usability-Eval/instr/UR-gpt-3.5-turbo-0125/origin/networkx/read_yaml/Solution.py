
import networkx as nx
import yaml

def read_graph_from_yaml(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    G = nx.from_dict_of_lists(data)
    return G

# Example usage:
path_to_yaml = 'graph.yaml'
graph = read_graph_from_yaml(path_to_yaml)
print(graph.nodes)
print(graph.edges)
