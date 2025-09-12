import networkx as nx
import yaml

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

# Convert the graph to a YAML formatted string
graph_yaml = yaml.dumpdict([(node, G[node].items()) for node in G.nodes()])

# Write to path
with open('graph.yaml', 'w') as file:
    file.write(graph_yaml)
