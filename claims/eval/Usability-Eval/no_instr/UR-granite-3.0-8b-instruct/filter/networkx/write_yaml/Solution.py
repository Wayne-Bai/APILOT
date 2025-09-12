import networkx as nx
import yaml

# Assuming G is your graph
G = nx.Graph()
# Add nodes and edges to G as needed

# Write graph G to YAML format to path
with open('graph.yaml', 'w') as f:
    yaml.dump(nx.node_link_data(G), f)
