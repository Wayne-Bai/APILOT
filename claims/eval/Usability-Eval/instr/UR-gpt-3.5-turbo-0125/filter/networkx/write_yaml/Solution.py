
import yaml
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')

# Define the output file path
output_path = 'output.yaml'

# Convert the graph to a dictionary and write to YAML file
graph_dict = nx.node_link_data(G)
with open(output_path, 'w') as f:
    yaml.dump(graph_dict, f)
