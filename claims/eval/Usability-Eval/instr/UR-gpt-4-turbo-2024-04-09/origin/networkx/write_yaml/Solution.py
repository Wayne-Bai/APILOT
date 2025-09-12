import networkx as nx
import yaml

def write_graph_to_yaml(G, path):
    # Convert Graph G to dictionary data
    graph_dict = nx.node_link_data(G)
    # Write the graph data to a YAML file
    with open(path, 'w') as file:
        yaml.dump(graph_dict, file)

# Example usage
G = nx.Graph()
G.add_edge('A', 'B')
G.add_node('C')

path = 'output_graph.yaml'
write_graph_to_yaml(G, path)
