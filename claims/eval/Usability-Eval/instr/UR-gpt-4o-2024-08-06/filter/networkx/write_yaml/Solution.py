import networkx as nx
import yaml

def write_graph_to_yaml(G, path):
    # Convert the graph G to a dictionary representation
    graph_data = nx.node_link_data(G)

    # Write the dictionary to a YAML file
    with open(path, 'w') as yaml_file:
        yaml.dump(graph_data, yaml_file, default_flow_style=False)

# Example usage
if __name__ == "__main__":
    # Create a simple test graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

    # Specify the path for the output YAML file
    path = "graph.yaml"

    # Write the graph to the YAML file
    write_graph_to_yaml(G, path)
