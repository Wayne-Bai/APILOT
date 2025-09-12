import networkx as nx
import yaml

def write_graph_to_yaml(graph, file_name):
    data = nx.readwrite.json_graph.node_link_data(graph)
    with open(file_name, 'w') as file:
        yaml.dump(data, file)

def read_graph_from_yaml(file_name):
    with open(file_name, 'r') as file:
        data = yaml.safe_load(file)
    return nx.readwrite.json_graph.node_link_graph(data)

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Write to YAML file
write_graph_to_yaml(G, 'graph.yaml')

# Read from YAML file
G_loaded = read_graph_from_yaml('graph.yaml')

