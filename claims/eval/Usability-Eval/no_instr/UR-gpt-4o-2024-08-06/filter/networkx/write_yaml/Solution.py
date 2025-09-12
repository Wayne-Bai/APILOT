import networkx as nx
import yaml

def write_graph_yaml(G, path):
    # Convert graph to a dictionary structure suited for YAML
    data = nx.node_link_data(G)
    
    # Write the YAML file
    with open(path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

# Example usage:
# Create a simple graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)

# Write this graph to a YAML file
write_graph_yaml(G, 'graph.yaml')
