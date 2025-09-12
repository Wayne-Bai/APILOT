import networkx as nx
import yaml

def write_graph_to_yaml(graph, filename):
    """Write the NetworkX graph to a YAML file."""
    with open(filename, 'w') as file:
        yaml.dump(nx.to_dict_of_lists(graph), file)

def read_graph_from_yaml(filename):
    """Read a NetworkX graph from a YAML file."""
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    graph = nx.from_dict_of_lists(data)
    return graph

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Write the graph to a YAML file
write_graph_to_yaml(G, 'graph.yaml')

# Read the graph from the YAML file
G_loaded = read_graph_from_yaml('graph.yaml')
