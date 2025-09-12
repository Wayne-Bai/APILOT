
import networkx as nx

# Read NetworkX graph from YAML format
def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        G = nx.node_link_graph(data)
    return G

# Write NetworkX graph to YAML format
def write_graph_to_yaml(G, file_path):
    data = nx.node_link_data(G)
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
