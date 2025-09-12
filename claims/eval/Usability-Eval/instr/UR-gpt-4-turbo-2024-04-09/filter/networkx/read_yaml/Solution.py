import networkx as nx
import yaml

def read_graph_from_yaml(path):
    with open(path, 'r') as file:
        # Load the YAML data
        data = yaml.safe_load(file)
        
    # Create a graph from the YAML data
    G = nx.node_link_graph(data)
    return G
