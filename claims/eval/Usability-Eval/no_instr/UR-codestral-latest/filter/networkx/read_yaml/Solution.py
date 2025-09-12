import networkx as nx
import yaml

# Read graph from YAML format
def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as stream:
        graph_data = yaml.safe_load(stream)
    G = nx.Graph(graph_data)
    return G

# Use the function
G = read_graph_from_yaml('your_file_path.yaml')
