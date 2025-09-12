
import networkx as nx
from networkx.readwrite import yaml

# Read a graph from a YAML file
with open('graph.yml', 'r') as f:
    G = yaml.read_yaml(f)

# Write a graph to a YAML file
with open('output.yml', 'w') as f:
    yaml.write_yaml(G, f)
