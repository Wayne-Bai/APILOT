import networkx as nx
import yaml

# Create a directed graph
G = nx.DiGraph()

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Convert the graph to a dictionary and serialize it in YAML format
data = nx.to_dict_of_dicts(G)
yaml_data = yaml.dump(data)

# Write the YAML data to a file
with open('graph.yaml', 'w') as f:
    f.write(yaml_data)
