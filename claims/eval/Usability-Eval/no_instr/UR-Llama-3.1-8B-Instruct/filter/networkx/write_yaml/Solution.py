import networkx as nx
import yaml

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Define a function to write the graph in YAML format
def write_graph_in_yaml(graph, path):
    data = nx.to_dict_of_dicts(graph)
    with open(path, 'w') as f:
        yaml.dump(data, f)

# Write the graph in YAML format
write_graph_in_yaml(G, 'graph.yaml')

print("Graph written in YAML format to graph.yaml")
