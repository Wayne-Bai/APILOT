import networkx as nx
import yaml

# Function to create a graph from YAML file
def create_graph_from_yaml(yaml_file):
    # Open the YAML file and load its content
    with open(yaml_file, 'r') as stream:
        data = yaml.safe_load(stream)

    # Create a new graph
    G = nx.Graph()

    # Add edges to the graph
    for edge in data['edges']:
        G.add_edge(edge[0], edge[1])

    # If the YAML data contains nodes information, add nodes to the graph
    if 'nodes' in data:
        G.add_nodes_from(data['nodes'])

    return G

# Use the function
G = create_graph_from_yaml('path_to_your_yaml_file.yaml')
