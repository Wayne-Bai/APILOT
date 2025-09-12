
# Read a NetworkX graph from a YAML file
with open('graph.yml', 'r') as f:
    G = nx.read_yaml(f)

# Write the NetworkX graph to a YAML file
with open('graph.yml', 'w') as f:
    nx.write_yaml(G, f)
