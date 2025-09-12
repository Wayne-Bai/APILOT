import yaml
import networkx as nx

# Read a YAML file into a NetworkX graph
with open("example.yaml", "r") as f:
    G = nx.parse_yaml(f)

# Write the NetworkX graph to a YAML file
with open("output.yaml", "w") as f:
    nx.write_yaml(G, f)
