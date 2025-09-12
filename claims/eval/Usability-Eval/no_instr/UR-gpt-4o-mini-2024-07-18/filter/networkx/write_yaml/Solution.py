import networkx as nx
import yaml

def save_graph_to_yaml(G, path):
    # Convert the graph to a dictionary
    graph_data = {
        "nodes": list(G.nodes(data=True)),
        "edges": list(G.edges(data=True))
    }
    
    # Write the dictionary to a YAML file
    with open(path, 'w') as yaml_file:
        yaml.dump(graph_data, yaml_file, default_flow_style=False)

# Example usage
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])
    save_graph_to_yaml(G, 'graph.yaml')
