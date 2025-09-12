import networkx as nx
import yaml

def write_graph_to_yaml(graph, file_path):
    # Convert the graph to an adjacency list
    adjacency_dict = nx.to_dict_of_dicts(graph)
    
    # Use yaml to write the adjacency list to a file
    with open(file_path, 'w') as f:
        yaml.dump(adjacency_dict, f)

def read_graph_from_yaml(file_path):
    # Read the adjacency list from a yaml file
    with open(file_path, 'r') as f:
        adjacency_dict = yaml.safe_load(f)
    
    # Convert the adjacency list back to a NetworkX graph
    graph = nx.from_dict_of_dicts(adjacency_dict)
    return graph

# Example usage:
if __name__ == "__main__":
    # Create a simple graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3)])

    # Specify a path for the YAML file
    yaml_file_path = 'graph.yaml'

    # Write the graph to a YAML file
    write_graph_to_yaml(G, yaml_file_path)

    # Read the graph back from the YAML file
    G_loaded = read_graph_from_yaml(yaml_file_path)

    # Output the edges of the loaded graph to verify
    print(list(G_loaded.edges))
