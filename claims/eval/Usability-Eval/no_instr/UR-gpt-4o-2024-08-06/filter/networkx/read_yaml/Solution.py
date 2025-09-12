import networkx as nx
import yaml

def read_graph_from_yaml(path):
    # Read YAML file
    with open(path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    
    # Create a NetworkX graph from the YAML data
    G = nx.node_link_graph(yaml_data)
    
    return G

# Example usage
# graph = read_graph_from_yaml("path_to_yaml_file.yaml")
# print(graph.nodes)
# print(graph.edges)
