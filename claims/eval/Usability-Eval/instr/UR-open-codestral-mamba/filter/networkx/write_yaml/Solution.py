import networkx as nx
import yaml

# Create graph G
G = nx.Graph()

# Add edges
G.add_edge(1, 2, weight=0.5)
G.add_edge(2, 3, weight=0.25)

# Write graph G to YAML file
with open('graph.yaml', 'w') as file:
    documents = yaml.dump(dict(G.edges(data=True)), file)
