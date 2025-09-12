import networkx as nx
import yaml

def write_graph_to_yaml(graph, filename):
    """
    Writes a NetworkX graph to a YAML file.

    Args:
        graph (nx.Graph): The graph to be written.
        filename (str): The filename for the YAML file.
    """
    graph_dict = nx.to_dict_of_dicts(graph)
    with open(filename, 'w') as file:
        yaml.dump(graph_dict, file, default_flow_style=False)

def read_graph_from_yaml(filename):
    """
    Reads a NetworkX graph from a YAML file.

    Args:
        filename (str): The filename of the YAML file.

    Returns:
        nx.Graph: The graph read from the YAML file.
    """
    with open(filename, 'r') as file:
        graph_dict = yaml.safe_load(file)
    graph = nx.from_dict_of_dicts(graph_dict)
    return graph

# Example usage
if __name__ == "__main__":
    # Create a graph
    G = nx.Graph()
    G.add_edge('A', 'B')
    G.add_edge('B', 'C')
    G.add_edge('C', 'A')

    # Write the graph to a YAML file
    write_graph_to_yaml(G, 'graph.yaml')

    # Read the graph from the YAML file
    loaded_G = read_graph_from_yaml('graph.yaml')

    # Print the loaded graph
    print(nx.to_dict_of_dicts(loaded_G))
