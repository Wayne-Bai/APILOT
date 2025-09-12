import networkx as nx
import yaml

# Function to write a NetworkX graph to a YAML file
def write_graph_to_yaml(graph, filename):
    with open(filename, 'w') as file:
        yaml.dump(nx.to_dict_of_lists(graph), file)

# Function to read a NetworkX graph from a YAML file
def read_graph_from_yaml(filename):
    with open(filename, 'r') as file:
        graph_data = yaml.load(file, Loader=yaml.FullLoader)
        graph = nx.from_dict_of_lists(graph_data)
    return graph

# Example usage
if __name__ == "__main__":
    # Creating a simple graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4)])

    # Writing the graph to a YAML file
    write_graph_to_yaml(G, 'graph.yaml')

    # Reading the graph back from the YAML file
    G_loaded = read_graph_from_yaml('graph.yaml')
    print(G_loaded.edges())
