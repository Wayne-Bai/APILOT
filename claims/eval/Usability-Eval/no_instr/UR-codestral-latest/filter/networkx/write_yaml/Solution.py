import networkx as nx
import yaml

# Create a graph
G = nx.Graph()

# Add nodes and edges...

# Specify the path
path = 'path_to_your_file.yaml'

# Write graph to YAML format
with open(path, 'w') as f:
    yaml.dump(nx.to_dict_of_dicts(G), f, default_flow_style=False)
