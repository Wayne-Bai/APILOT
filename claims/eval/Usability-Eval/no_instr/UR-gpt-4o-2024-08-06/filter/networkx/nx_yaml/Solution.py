import networkx as nx
import yaml

# Function to write a NetworkX graph to a YAML file
def write_graph_to_yaml(graph, file_path):
    graph_data = nx.node_link_data(graph)
    with open(file_path, 'w') as yaml_file:
        yaml.dump(graph_data, yaml_file)

# Function to read a NetworkX graph from a YAML file
def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as yaml_file:
        graph_data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    graph = nx.node_link_graph(graph_data)
    return graph

# Example usage
if __name__ == "__main__":
    # Create an example graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])

    # Write the graph to a YAML file
    write_graph_to_yaml(G, 'graph.yaml')

    # Read the graph back from the YAML file
    G_loaded = read_graph_from_yaml('graph.yaml')

    # Print edges of the loaded graph
    print(list(G_loaded.edges()))
