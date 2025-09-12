import networkx as nx
import yaml

# Create a new graph G
G = nx.Graph()

# Add nodes and edges
G.add_node(1, name="Node1", attribute="value1")
G.add_node(2, name="Node2", attribute="value2")
G.add_edge(1, 2, weight=4.5)

# Convert G to a dictionary
data = nx.readwrite.json_graph.node_link_data(G)

# Write the graph to a YAML file
path = 'path_to_yaml_file.yaml'
with open(path, 'w') as file:
    yaml.dump(data, file)
