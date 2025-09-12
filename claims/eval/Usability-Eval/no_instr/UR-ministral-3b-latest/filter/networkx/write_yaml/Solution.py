import networkx as nx
import yaml

# Example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Write graph to YAML file
with open('graph.yml', 'w') as file:
    yaml.dump(G, file)

