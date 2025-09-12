
import networkx as nx
import yaml

# Read a NetworkX graph from a YAML file
with open('graph.yaml', 'r') as f:
    G = nx.read_yaml(f)

# Write the NetworkX graph to a YAML file
with open('graph.yaml', 'w') as f:
    nx.write_yaml(G, f)
