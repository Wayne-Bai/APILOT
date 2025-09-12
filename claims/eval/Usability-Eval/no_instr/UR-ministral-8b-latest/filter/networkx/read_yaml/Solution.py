import yaml
import networkx as nx

def read_graph_from_yaml(file_path):
    # Read the graph in YAML format
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Create a graph from the data
    G = nx.Graph()
    for node, attributes in data['nodes'].items():
        G.add_node(node)
        for key, value in attributes.items():
            G.nodes[node][key] = value

    for edge in data['edges']:
        G.add_edge(edge[0], edge[1])

    return G

# Usage example
# replace 'path_to_yaml_file.yaml' with the actual file path
file_path = 'path_to_yaml_file.yaml'
graph = read_graph_from_yaml(file_path)
