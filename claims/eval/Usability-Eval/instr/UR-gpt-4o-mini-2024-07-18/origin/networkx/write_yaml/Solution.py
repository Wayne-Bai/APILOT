import networkx as nx
import yaml

def write_graph_to_yaml(G, path):
    # Convert graph G to a dictionary representation
    graph_data = nx.to_dict_of_lists(G)
    # Write the graph data to a YAML file
    with open(path, 'w') as yaml_file:
        yaml.dump(graph_data, yaml_file)

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4)])

    # Write the graph to a YAML file
    write_graph_to_yaml(G, 'graph.yaml')
