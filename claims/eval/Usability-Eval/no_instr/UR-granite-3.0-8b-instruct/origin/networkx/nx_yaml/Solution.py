import networkx as nx
import yaml

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Write the graph to a YAML file
with open('graph.yaml', 'w') as f:
    yaml.dump(nx.node_link_data(G), f)

# Read the graph from a YAML file
with open('graph.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Create a new graph from the YAML data
H = nx.node_link_graph(data)

# Print the nodes and edges of the new graph
print("Nodes:", H.nodes())
print("Edges:", H.edges())
