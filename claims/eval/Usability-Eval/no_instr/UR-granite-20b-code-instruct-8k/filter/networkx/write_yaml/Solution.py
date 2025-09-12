import networkx as nx
import yaml

def write_yaml(G, path):
    # Check if path is valid
    try:
        with open(path, 'w') as f:
            # Write graph G in YAML format to path
            yaml.dump(nx.readwrite.json_graph.node_link_data(G), f)
    except IOError:
        print("Error: Unable to write to path")
