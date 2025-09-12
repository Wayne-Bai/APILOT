import yaml
import networkx as nx

def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    G = nx.Graph()

    for node in data['nodes']:
        G.add_node(node)

    for edge in data['edges']:
        G.add_edge(edge['source'], edge['destination'])

    return G

# Example usage:
# graph_data = read_graph_from_yaml('graph.yaml')
