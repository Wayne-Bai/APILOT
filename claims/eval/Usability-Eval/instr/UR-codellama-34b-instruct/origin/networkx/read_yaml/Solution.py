import yaml
from networkx import MultiDiGraph, nx_pyyaml

# Load the YAML file into a dictionary
with open('graph.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Create a NetworkX graph from the dictionary
G = MultiDiGraph()
nx_pyyaml.read_multi_digraph(data, G)
