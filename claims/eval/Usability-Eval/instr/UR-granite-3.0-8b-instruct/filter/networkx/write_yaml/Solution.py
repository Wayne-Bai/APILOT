import networkx as nx
import yaml

# Assuming G is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('Node1', 'Node2')
G.add_edge('Node2', 'Node3')

# Write graph to YAML format
with open('graph.yaml', 'w') as file:
    yaml.dump(nx.node_link_data(G), file)
