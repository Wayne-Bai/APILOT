import ruamel.yaml
import networkx as nx

def read_graph_from_yaml(file_path):
    # Load YAML data
    with open(file_path, 'r') as file:
        yaml_data = ruamel.yaml.safe_load(file)

    # Create a directed graph
    graph = nx.DiGraph()

    # Add nodes and edges to the graph
    for node, edges in yaml_data.items():
        graph.add_node(node)
        for neighbor, weight in edges.items():
            graph.add_edge(node, neighbor, weight=weight)

    return graph

# Example usage:
file_path = "path/to/your/graph.yaml"
graph = read_graph_from_yaml(file_path)
