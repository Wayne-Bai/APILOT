
import networkx as nx
import yaml

# Create a sample graph
G = nx.gnp_random_graph(10, 0.5)

# Write the graph to a YAML file
with open("graph.yaml", "w") as f:
    yaml.dump(nx.readwrite.graph_to_data(G), f)
