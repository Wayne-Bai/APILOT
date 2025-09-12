import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    graph = nx.MultiDiGraph()

    for node in data['nodes']:
        graph.add_node(node['id'], pos=node['pos'])

    for edge in data['edges']:
        graph.add_edge(edge['source'], edge['target'], weight=edge['weight'])

    return graph

# Read a graph from a YAML file specified by `file_path`
file_path = 'path/to/your/graph.yaml'  # Replace with your actual file path
graph = read_graph_from_yaml(file_path)
