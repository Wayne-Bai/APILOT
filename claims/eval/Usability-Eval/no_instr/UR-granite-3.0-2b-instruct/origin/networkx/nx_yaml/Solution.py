import networkx as nx
import yaml

# Load a graph from a YAML file
with open('graph.yaml', 'r') as file:
    G = nx.from_yaml(file)

# Write a graph to a YAML file
dump = yaml.dump(G)
with open('graph.yaml', 'w') as file:
    file.write(dump)
