import networkx as nx
import yaml

# Function to write a graph to a YAML file
def write_graph_to_yaml(graph, file_name):
    data = nx.node_link_data(graph)  # convert graph to node-link format for serialization
    with open(file_name, 'w') as file:
        yaml.dump(data, file)

# Function to read a graph from a YAML file
def read_graph_from_yaml(file_name):
    with open(file_name, 'r') as file:
        data = yaml.safe_load(file)  # load the data from YAML file
    graph = nx.node_link_graph(data)  # convert node-link format to graph
    return graph

# Example: Creating a graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Write the graph to a YAML file
write_graph_to_yaml(G, 'example_graph.yaml')

# Read the graph from a YAML file
loaded_graph = read_graph_from_yaml('example_graph.yaml')
print(loaded_graph.edges())
