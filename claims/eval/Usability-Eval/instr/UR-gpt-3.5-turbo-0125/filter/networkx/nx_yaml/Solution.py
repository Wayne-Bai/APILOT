
import yaml
import networkx as nx

def write_yaml(graph, file_path):
    data = nx.readwrite.yaml.GraphYAMLEncoder().default(graph)
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        graph = nx.readwrite.yaml.GraphYAMLDecoder().object_hook(data)
    return graph

# Create a sample graph
G = nx.path_graph(5)

# Write the graph to a YAML file
write_yaml(G, 'graph.yaml')

# Read the graph from the YAML file
G_read = read_yaml('graph.yaml')

print("Nodes of the graph:", G_read.nodes())
